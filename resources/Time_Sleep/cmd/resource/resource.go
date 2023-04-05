package resource

import (
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
	resourceType := "AwsCommunity::Time::Sleep"
	resourceTypeSplits := strings.Split(resourceType, "::")
	return fmt.Sprintf("/CloudFormation/%s/%s/%s/%s", resourceTypeSplits[0], resourceTypeSplits[1], resourceTypeSplits[2], *model.Id)
}

// Create handles the Create event from the Cloudformation service.
func Create(req handler.Request, _ *Model, currentModel *Model) (handler.ProgressEvent, error) {

	id := uuid.New().String()
	currentModel.Id = &id

	// Save the unique identifier in SSM if it exists its a duplicate
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

	if currentModel.SleepOnCreate == nil || *currentModel.SleepOnCreate {
		time.Sleep(time.Duration(*currentModel.Seconds * int(time.Second)))
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

	response := handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Read complete",
		ResourceModel:   currentModel,
	}

	return response, nil
}

// Update handles the Update event from the Cloudformation service.
func Update(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	// See if the SSM parameter exists to determine if the resource exists
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

	if currentModel.SleepOnUpdate == nil || *currentModel.SleepOnUpdate {
		time.Sleep(time.Duration(*currentModel.Seconds * int(time.Second)))
	}
	time.Sleep(time.Duration(*currentModel.Seconds * int(time.Second)))

	response := handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Update complete",
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

	if currentModel.SleepOnDelete == nil || *currentModel.SleepOnDelete {
		time.Sleep(time.Duration(*currentModel.Seconds * int(time.Second)))
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
