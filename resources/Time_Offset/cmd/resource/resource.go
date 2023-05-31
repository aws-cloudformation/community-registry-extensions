package resource

import (
	"encoding/json"
	"errors"
	"fmt"
	"strings"
	"time"

	"github.com/aws-cloudformation/cloudformation-cli-go-plugin/cfn/handler"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/service/cloudformation"
	"github.com/aws/aws-sdk-go/service/ssm"
	"github.com/google/uuid"
)

func buildSsmParameterString(model *Model) string {
	resourceType := "AwsCommunity::Time::Offset"
	resourceTypeSplits := strings.Split(resourceType, "::")
	return fmt.Sprintf("/CloudFormation/%s/%s/%s/%s", resourceTypeSplits[0], resourceTypeSplits[1], resourceTypeSplits[2], *model.Id)
}

// Create handles the Create event from the Cloudformation service.
func Create(req handler.Request, _ *Model, currentModel *Model) (handler.ProgressEvent, error) {

	// If Time isn't specified we use now
	if currentModel.Time == nil {
		now := timeToString(time.Now())
		currentModel.Time = &now
	}
	id := uuid.New().String()
	currentModel.Id = &id

	// determine the offset
	t, err := updateTimeWithOffset(currentModel)
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			Message:          err.Error(),
			HandlerErrorCode: cloudformation.HandlerErrorCodeAlreadyExists,
			ResourceModel:    nil,
		}, nil
	}

	// convert a timestamp into the model so we have all the attributes
	timeToModel(currentModel, t)

	// Save the unique identifier in SSM if it exists its a duplicate
	ssmParameter := buildSsmParameterString(currentModel)
	svc := ssm.New(req.Session)
	jsonData, _ := json.Marshal(currentModel)
	_, err = svc.PutParameter(&ssm.PutParameterInput{
		Name:      &ssmParameter,
		Value:     aws.String(string(jsonData)),
		Overwrite: aws.Bool(false),
		Tier:      aws.String("Standard"),
		Type:      aws.String("String"),
	})
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			Message:          err.Error(),
			HandlerErrorCode: cloudformation.HandlerErrorCodeAlreadyExists,
			ResourceModel:    nil,
		}, nil
	}

	response := handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Create complete",
		ResourceModel:   currentModel,
	}
	return response, nil
}

// Read handles the Read event from the Cloudformation service.
func Read(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	// See if the SSM parameter exists to determine if the resource exists
	ssmParameter := buildSsmParameterString(currentModel)
	svc := ssm.New(req.Session)
	p, err := svc.GetParameter(&ssm.GetParameterInput{
		Name: &ssmParameter,
	})
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
			Message:          "Resource not found",
		}, nil
	}

	err = json.Unmarshal([]byte(*p.Parameter.Value), currentModel)
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeInternalFailure,
			Message:          "Error decoding SSM parameter value",
		}, nil
	}
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			Message:          err.Error(),
			HandlerErrorCode: cloudformation.HandlerErrorCodeAlreadyExists,
			ResourceModel:    nil,
		}, nil
	}

	response := handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Read complete",
		ResourceModel:   currentModel,
	}

	return response, nil
}

// Update handles the Update event from the Cloudformation service.
func Update(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	// Validate teh Id exists already
	ssmParameter := buildSsmParameterString(currentModel)
	svc := ssm.New(req.Session)
	_, err := svc.GetParameter(&ssm.GetParameterInput{
		Name: &ssmParameter,
	})
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			Message:          err.Error(),
			HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
			ResourceModel:    nil,
		}, nil
	}

	// If Time isn't specified we use now
	if currentModel.Time == nil {
		now := timeToString(time.Now())
		currentModel.Time = &now
	}

	// determine the offset
	t, err := updateTimeWithOffset(currentModel)
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			Message:          err.Error(),
			HandlerErrorCode: cloudformation.HandlerErrorCodeInternalFailure,
			ResourceModel:    nil,
		}, nil
	}

	// convert a timestamp into the model so we have all the attributes
	timeToModel(currentModel, t)

	// Save the unique identifier in SSM if it exists its a duplicate
	jsonData, _ := json.Marshal(currentModel)
	_, err = svc.PutParameter(&ssm.PutParameterInput{
		Name:      &ssmParameter,
		Value:     aws.String(string(jsonData)),
		Overwrite: aws.Bool(true),
		Tier:      aws.String("Standard"),
		Type:      aws.String("String"),
	})
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			Message:          err.Error(),
			HandlerErrorCode: cloudformation.HandlerErrorCodeInternalFailure,
			ResourceModel:    nil,
		}, nil
	}

	response := handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Create complete",
		ResourceModel:   currentModel,
	}
	return response, nil
}

// Delete handles the Delete event from the Cloudformation service.
func Delete(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	// See if the SSM parameter exists to determine if the resource exists
	ssmParameter := buildSsmParameterString(currentModel)
	svc := ssm.New(req.Session)
	_, err := svc.DeleteParameter(&ssm.DeleteParameterInput{
		Name: &ssmParameter,
	})
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
			Message:          "Resource not found",
		}, nil
	}

	response := handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Delete complete",
		ResourceModel:   nil,
	}

	return response, nil
}

// List handles the List event from the Cloudformation service.
func List(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {
	return handler.ProgressEvent{}, errors.New("this resource type does not support list")
}

// Convert time to a string
func timeToString(t time.Time) string {
	return t.Format(time.RFC3339)
}

func updateTimeWithOffset(m *Model) (*time.Time, error) {

	t, err := time.Parse(time.RFC3339, *m.Time)
	if err != nil {
		return nil, err
	}

	if m.OffsetDays != nil {
		t = t.AddDate(0, 0, *m.OffsetDays)
	}
	if m.OffsetMonths != nil {
		t = t.AddDate(0, *m.OffsetMonths, 0)
	}
	if m.OffsetYears != nil {
		t = t.AddDate(*m.OffsetYears, 0, 0)
	}
	if m.OffsetHours != nil {
		t = t.Add(time.Hour * time.Duration(*m.OffsetHours))
	}
	if m.OffsetMinutes != nil {
		t = t.Add(time.Minute * time.Duration(*m.OffsetMinutes))
	}
	if m.OffsetSeconds != nil {
		t = t.Add(time.Second * time.Duration(*m.OffsetSeconds))
	}

	return &t, nil

}

// Convert time into a model
func timeToModel(m *Model, t *time.Time) {

	utc := t.Format(time.RFC3339)
	day := fmt.Sprintf("%02d", t.Day())
	hour := fmt.Sprintf("%02d", t.Hour())
	minute := fmt.Sprintf("%02d", t.Minute())
	month := fmt.Sprintf("%02d", int(t.Month()))
	second := fmt.Sprintf("%02d", t.Second())
	unix := fmt.Sprintf("%02d", int(t.Unix()))
	year := fmt.Sprintf("%02d", t.Year())

	m.Utc = &utc
	m.Day = &day
	m.Hour = &hour
	m.Minute = &minute
	m.Month = &month
	m.Second = &second
	m.Unix = &unix
	m.Year = &year

}
