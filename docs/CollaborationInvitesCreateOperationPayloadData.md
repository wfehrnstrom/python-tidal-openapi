# CollaborationInvitesCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | [**CollaborationInvitesCreateOperationPayloadDataRelationships**](CollaborationInvitesCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.collaboration_invites_create_operation_payload_data import CollaborationInvitesCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesCreateOperationPayloadData from a JSON string
collaboration_invites_create_operation_payload_data_instance = CollaborationInvitesCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesCreateOperationPayloadData.to_json())

# convert the object into a dict
collaboration_invites_create_operation_payload_data_dict = collaboration_invites_create_operation_payload_data_instance.to_dict()
# create an instance of CollaborationInvitesCreateOperationPayloadData from a dict
collaboration_invites_create_operation_payload_data_from_dict = CollaborationInvitesCreateOperationPayloadData.from_dict(collaboration_invites_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


