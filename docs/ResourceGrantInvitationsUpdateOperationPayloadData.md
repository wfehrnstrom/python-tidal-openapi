# ResourceGrantInvitationsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceGrantInvitationsUpdateOperationPayloadDataAttributes**](ResourceGrantInvitationsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.resource_grant_invitations_update_operation_payload_data import ResourceGrantInvitationsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsUpdateOperationPayloadData from a JSON string
resource_grant_invitations_update_operation_payload_data_instance = ResourceGrantInvitationsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsUpdateOperationPayloadData.to_json())

# convert the object into a dict
resource_grant_invitations_update_operation_payload_data_dict = resource_grant_invitations_update_operation_payload_data_instance.to_dict()
# create an instance of ResourceGrantInvitationsUpdateOperationPayloadData from a dict
resource_grant_invitations_update_operation_payload_data_from_dict = ResourceGrantInvitationsUpdateOperationPayloadData.from_dict(resource_grant_invitations_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


