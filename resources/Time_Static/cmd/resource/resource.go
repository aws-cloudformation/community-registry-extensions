package resource

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"strings"
	"time"

	"github.com/aws-cloudformation/cloudformation-cli-go-plugin/cfn/handler"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/service/cloudformation"
	"github.com/aws/aws-sdk-go/service/ssm"
	"github.com/google/uuid"
)

func buildSsmParameterString(model *Model) string {
	resourceType := "AwsCommunity::Time::Static"
	resourceTypeSplits := strings.Split(resourceType, "::")
	return fmt.Sprintf("/CloudFormation/%s/%s/%s/%s", resourceTypeSplits[0], resourceTypeSplits[1], resourceTypeSplits[2], *model.Id)
}

// Create handles the Create event from the Cloudformation service.
func Create(req handler.Request, _ *Model, currentModel *Model) (handler.ProgressEvent, error) {

	if currentModel.Time == nil {
		now := timeToString(time.Now())
		currentModel.Time = &now
	}
	id := uuid.New().String()
	currentModel.Id = &id

	timeToModel(currentModel)

	ssmParameter := buildSsmParameterString(currentModel)
	svc := ssm.New(req.Session)
	_, err := svc.PutParameter(&ssm.PutParameterInput{
		Name:      &ssmParameter,
		Value:     &id,
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

	logModel("Create Response: ", response)
	return response, nil
}

// Read handles the Read event from the Cloudformation service.
func Read(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	logModel("Read Current Model: ", currentModel)

	ssmParameter := buildSsmParameterString(currentModel)

	svc := ssm.New(req.Session)
	_, err := svc.GetParameter(&ssm.GetParameterInput{
		Name: &ssmParameter,
	})
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
			Message:          "Resource not found",
		}, nil
	}

	if currentModel.Id == nil {
		fmt.Println("Resource not found")
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
			Message:          "Resource not found",
		}, nil
	}

	timeToModel(currentModel)

	response := handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Read complete",
		ResourceModel:   currentModel,
	}

	logModel("Read Response: ", response)
	return response, nil
}

// Update handles the Update event from the Cloudformation service.
func Update(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	logModel("Update Current Model: ", currentModel)
	if prevModel.Id == nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
			Message:          "Resource not found",
		}, nil
	}

	ssmParameter := buildSsmParameterString(currentModel)

	svc := ssm.New(req.Session)
	_, err := svc.GetParameter(&ssm.GetParameterInput{
		Name: &ssmParameter,
	})
	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
			Message:          "Resource not found",
		}, nil
	}

	timeToModel(currentModel)

	response := handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Update complete",
		ResourceModel:   currentModel,
	}

	logModel("Update Response: ", response)
	return response, nil
}

// Delete handles the Delete event from the Cloudformation service.
func Delete(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	logModel("Delete Current Model: ", currentModel)

	if currentModel.Id == nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
			Message:          "Resource not found",
		}, nil
	}

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

	logModel("Delete Response: ", response)
	return response, nil
}

// List handles the List event from the Cloudformation service.
func List(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	return handler.ProgressEvent{}, errors.New("this resource type does not support list")
}

func logModel(m string, i interface{}) {
	responseString, _ := json.Marshal(i)
	log.Printf("%s: %s", m, responseString)
}

func timeToString(t time.Time) string {
	return t.Format(time.RFC3339)
}

func timeToModel(m *Model) error {

	t, err := time.Parse(time.RFC3339, *m.Time)
	if err != nil {
		return err
	}

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

	return nil
}
