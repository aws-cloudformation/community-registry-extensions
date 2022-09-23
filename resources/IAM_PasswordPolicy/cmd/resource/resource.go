package resource

import (
	"errors"
	"fmt"

	"github.com/aws-cloudformation/cloudformation-cli-go-plugin/cfn/handler"
	"github.com/aws/aws-sdk-go/aws/awserr"
	"github.com/aws/aws-sdk-go/service/cloudformation"
	"github.com/aws/aws-sdk-go/service/iam"
)

// Create handles the Create event from the Cloudformation service.
func Create(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {
	normalizeModel(currentModel)

	client := iam.New(req.Session)
	_, err := getPasswordPolicy(client)

	if err != nil {
		if aerr, ok := err.(awserr.Error); ok {
			switch aerr.Code() {
			case iam.ErrCodeNoSuchEntityException:
				MaxPasswordAge := newIntToInt64(currentModel.MaxPasswordAge)
				MinimumPasswordLength := newIntToInt64(currentModel.MinimumPasswordLength)
				PasswordReusePrevention := newIntToInt64(currentModel.PasswordReusePrevention)
				_, err := client.UpdateAccountPasswordPolicy(&iam.UpdateAccountPasswordPolicyInput{
					AllowUsersToChangePassword: currentModel.AllowUsersToChangePassword,
					HardExpiry:                 currentModel.HardExpiry,
					MaxPasswordAge:             MaxPasswordAge,
					MinimumPasswordLength:      MinimumPasswordLength,
					PasswordReusePrevention:    PasswordReusePrevention,
					RequireLowercaseCharacters: currentModel.RequireLowercaseCharacters,
					RequireNumbers:             currentModel.RequireNumbers,
					RequireSymbols:             currentModel.RequireSymbols,
					RequireUppercaseCharacters: currentModel.RequireLowercaseCharacters,
				})

				if err != nil {
					return handler.ProgressEvent{
						OperationStatus:  handler.Failed,
						HandlerErrorCode: cloudformation.HandlerErrorCodeHandlerInternalFailure,
						Message:          fmt.Sprintf("Create failed: %s", err),
					}, nil
				}
				currentModel.AccountId = &req.RequestContext.AccountID

				return handler.ProgressEvent{
					OperationStatus: handler.Success,
					Message:         "Create complete",
					ResourceModel:   currentModel,
				}, nil
			}
		}

		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			Message:          fmt.Sprintf("Create failed: %s", err),
			HandlerErrorCode: cloudformation.HandlerErrorCodeInternalFailure,
		}, err
	}

	// Not implemented, return an empty handler.ProgressEvent
	// and an error
	return handler.ProgressEvent{
		OperationStatus: handler.Failed,
		Message:         "The accounts password policy is already set",
	}, errors.New("the accounts password policy is already set")
}

// Read handles the Read event from the Cloudformation service.
func Read(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	client := iam.New(req.Session)
	m, err := getPasswordPolicy(client)

	if err != nil {
		if aerr, ok := err.(awserr.Error); ok {
			switch aerr.Code() {
			case iam.ErrCodeNoSuchEntityException:
				return handler.ProgressEvent{
					OperationStatus:  handler.Failed,
					HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
					Message:          fmt.Sprintf("Read failed: %s", err),
				}, nil
			}
		}

		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeInternalFailure,
			Message:          fmt.Sprintf("Create failed: %s", err),
		}, err
	}

	m.AccountId = &req.RequestContext.AccountID
	normalizeModel(m)
	return handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Read Complete",
		ResourceModel:   m,
	}, nil
}

// Update handles the Update event from the Cloudformation service.
func Update(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {
	normalizeModel(currentModel)

	client := iam.New(req.Session)
	_, err := getPasswordPolicy(client)

	if err != nil {
		if aerr, ok := err.(awserr.Error); ok {
			switch aerr.Code() {
			case iam.ErrCodeNoSuchEntityException:
				return handler.ProgressEvent{
					OperationStatus:  handler.Failed,
					Message:          "Policy not found",
					HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
				}, nil
			}
		}

		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeInternalFailure,
			Message:          fmt.Sprintf("Create failed: %s", err),
		}, err
	}

	MaxPasswordAge := newIntToInt64(currentModel.MaxPasswordAge)
	MinimumPasswordLength := newIntToInt64(currentModel.MinimumPasswordLength)
	PasswordReusePrevention := newIntToInt64(currentModel.PasswordReusePrevention)
	_, err = client.UpdateAccountPasswordPolicy(&iam.UpdateAccountPasswordPolicyInput{
		AllowUsersToChangePassword: currentModel.AllowUsersToChangePassword,
		HardExpiry:                 currentModel.HardExpiry,
		MaxPasswordAge:             MaxPasswordAge,
		MinimumPasswordLength:      MinimumPasswordLength,
		PasswordReusePrevention:    PasswordReusePrevention,
		RequireLowercaseCharacters: currentModel.RequireLowercaseCharacters,
		RequireNumbers:             currentModel.RequireNumbers,
		RequireSymbols:             currentModel.RequireSymbols,
		RequireUppercaseCharacters: currentModel.RequireLowercaseCharacters,
	})

	if err != nil {
		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeHandlerInternalFailure,
			Message:          fmt.Sprintf("Update failed: %s", err),
		}, nil
	}
	currentModel.AccountId = &req.RequestContext.AccountID

	return handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Update complete",
		ResourceModel:   currentModel,
	}, nil

}

// Delete handles the Delete event from the Cloudformation service.
func Delete(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {

	client := iam.New(req.Session)

	_, err := client.DeleteAccountPasswordPolicy(&iam.DeleteAccountPasswordPolicyInput{})

	if err != nil {
		if aerr, ok := err.(awserr.Error); ok {
			fmt.Printf("AWS error")
			switch aerr.Code() {
			case iam.ErrCodeNoSuchEntityException:
				return handler.ProgressEvent{
					OperationStatus:  handler.Failed,
					HandlerErrorCode: cloudformation.HandlerErrorCodeNotFound,
					Message:          "Create complete",
					ResourceModel:    currentModel,
				}, nil
			}
		}

		return handler.ProgressEvent{
			OperationStatus:  handler.Failed,
			HandlerErrorCode: cloudformation.HandlerErrorCodeHandlerInternalFailure,
			Message:          fmt.Sprintf("Create failed: %s", err),
		}, err
	}

	return handler.ProgressEvent{
		OperationStatus: handler.Success,
		Message:         "Delete Complete",
	}, err
}

// List handles the List event from the Cloudformation service.
func List(req handler.Request, prevModel *Model, currentModel *Model) (handler.ProgressEvent, error) {
	return handler.ProgressEvent{}, errors.New("not implemented: list")
}

func getPasswordPolicy(c *iam.IAM) (*Model, error) {

	fmt.Printf("Get PasswordPolicy\n")
	result, err := c.GetAccountPasswordPolicy(&iam.GetAccountPasswordPolicyInput{})

	if err != nil {
		fmt.Printf("Get Error\n")
		return nil, err
	}

	return &Model{
		AllowUsersToChangePassword: result.PasswordPolicy.AllowUsersToChangePassword,
		HardExpiry:                 result.PasswordPolicy.HardExpiry,
		MaxPasswordAge:             newInt64ToInt(result.PasswordPolicy.MaxPasswordAge),
		MinimumPasswordLength:      newInt64ToInt(result.PasswordPolicy.MinimumPasswordLength),
		PasswordReusePrevention:    newInt64ToInt(result.PasswordPolicy.PasswordReusePrevention),
		RequireLowercaseCharacters: result.PasswordPolicy.RequireLowercaseCharacters,
		RequireNumbers:             result.PasswordPolicy.RequireNumbers,
		RequireSymbols:             result.PasswordPolicy.RequireSymbols,
		RequireUppercaseCharacters: result.PasswordPolicy.RequireUppercaseCharacters,
	}, nil

}

func newBool(b bool) *bool {
	newB := b
	return &newB
}

func newInt(i int) *int {
	newI := i
	return &newI
}

func newInt64ToInt(i *int64) *int {
	if i != nil {
		newI := int(*i)
		return &newI
	}

	return nil
}

func newIntToInt64(i *int) *int64 {
	if i != nil {
		newI := int64(*i)
		return &newI
	}

	return nil
}

func normalizeModel(m *Model) {
	if m.AllowUsersToChangePassword == nil {
		m.AllowUsersToChangePassword = newBool(false)
	}
	if m.HardExpiry == nil {
		m.HardExpiry = newBool(false)
	}
	if m.MaxPasswordAge != nil {
		n := int64(*m.MaxPasswordAge)
		m.MaxPasswordAge = newInt64ToInt(&n)
	}
	if m.MinimumPasswordLength == nil {
		m.MinimumPasswordLength = newInt(6)
	}
	if m.PasswordReusePrevention != nil {
		n := int64(*m.PasswordReusePrevention)
		m.PasswordReusePrevention = newInt64ToInt(&n)
	}
	if m.RequireLowercaseCharacters == nil {
		m.RequireLowercaseCharacters = newBool(false)
	}
	if m.RequireNumbers == nil {
		m.RequireNumbers = newBool(false)
	}
	if m.RequireSymbols == nil {
		m.RequireSymbols = newBool(false)
	}
	if m.RequireUppercaseCharacters == nil {
		m.RequireUppercaseCharacters = newBool(false)
	}
}
