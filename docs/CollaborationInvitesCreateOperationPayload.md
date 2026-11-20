# CollaborationInvitesCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CollaborationInvitesCreateOperationPayloadData**](CollaborationInvitesCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.collaboration_invites_create_operation_payload import CollaborationInvitesCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesCreateOperationPayload from a JSON string
collaboration_invites_create_operation_payload_instance = CollaborationInvitesCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesCreateOperationPayload.to_json())

# convert the object into a dict
collaboration_invites_create_operation_payload_dict = collaboration_invites_create_operation_payload_instance.to_dict()
# create an instance of CollaborationInvitesCreateOperationPayload from a dict
collaboration_invites_create_operation_payload_from_dict = CollaborationInvitesCreateOperationPayload.from_dict(collaboration_invites_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


