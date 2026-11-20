# ResourceGrantInvitationsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantInvitationsCreateOperationPayloadData**](ResourceGrantInvitationsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.resource_grant_invitations_create_operation_payload import ResourceGrantInvitationsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsCreateOperationPayload from a JSON string
resource_grant_invitations_create_operation_payload_instance = ResourceGrantInvitationsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsCreateOperationPayload.to_json())

# convert the object into a dict
resource_grant_invitations_create_operation_payload_dict = resource_grant_invitations_create_operation_payload_instance.to_dict()
# create an instance of ResourceGrantInvitationsCreateOperationPayload from a dict
resource_grant_invitations_create_operation_payload_from_dict = ResourceGrantInvitationsCreateOperationPayload.from_dict(resource_grant_invitations_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


