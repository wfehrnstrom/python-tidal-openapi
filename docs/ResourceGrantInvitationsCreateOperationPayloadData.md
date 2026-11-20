# ResourceGrantInvitationsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceGrantInvitationsCreateOperationPayloadDataAttributes**](ResourceGrantInvitationsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**ResourceGrantInvitationsCreateOperationPayloadDataRelationships**](ResourceGrantInvitationsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.resource_grant_invitations_create_operation_payload_data import ResourceGrantInvitationsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsCreateOperationPayloadData from a JSON string
resource_grant_invitations_create_operation_payload_data_instance = ResourceGrantInvitationsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsCreateOperationPayloadData.to_json())

# convert the object into a dict
resource_grant_invitations_create_operation_payload_data_dict = resource_grant_invitations_create_operation_payload_data_instance.to_dict()
# create an instance of ResourceGrantInvitationsCreateOperationPayloadData from a dict
resource_grant_invitations_create_operation_payload_data_from_dict = ResourceGrantInvitationsCreateOperationPayloadData.from_dict(resource_grant_invitations_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


