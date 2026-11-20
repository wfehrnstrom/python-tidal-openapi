# ResourceGrantInvitationsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantInvitationsUpdateOperationPayloadData**](ResourceGrantInvitationsUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.resource_grant_invitations_update_operation_payload import ResourceGrantInvitationsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsUpdateOperationPayload from a JSON string
resource_grant_invitations_update_operation_payload_instance = ResourceGrantInvitationsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsUpdateOperationPayload.to_json())

# convert the object into a dict
resource_grant_invitations_update_operation_payload_dict = resource_grant_invitations_update_operation_payload_instance.to_dict()
# create an instance of ResourceGrantInvitationsUpdateOperationPayload from a dict
resource_grant_invitations_update_operation_payload_from_dict = ResourceGrantInvitationsUpdateOperationPayload.from_dict(resource_grant_invitations_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


