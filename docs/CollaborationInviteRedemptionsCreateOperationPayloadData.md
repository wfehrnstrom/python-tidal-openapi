# CollaborationInviteRedemptionsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | [**CollaborationInviteRedemptionsCreateOperationPayloadDataRelationships**](CollaborationInviteRedemptionsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.collaboration_invite_redemptions_create_operation_payload_data import CollaborationInviteRedemptionsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInviteRedemptionsCreateOperationPayloadData from a JSON string
collaboration_invite_redemptions_create_operation_payload_data_instance = CollaborationInviteRedemptionsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(CollaborationInviteRedemptionsCreateOperationPayloadData.to_json())

# convert the object into a dict
collaboration_invite_redemptions_create_operation_payload_data_dict = collaboration_invite_redemptions_create_operation_payload_data_instance.to_dict()
# create an instance of CollaborationInviteRedemptionsCreateOperationPayloadData from a dict
collaboration_invite_redemptions_create_operation_payload_data_from_dict = CollaborationInviteRedemptionsCreateOperationPayloadData.from_dict(collaboration_invite_redemptions_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


