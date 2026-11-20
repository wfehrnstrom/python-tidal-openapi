# ResourceGrantInvitationsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password a user must send to redeem. Never returned. Must be printable ASCII characters. A value sets or changes it; null removes it; omitted leaves it unchanged. Playlist invitations cannot have one. | [optional] 
**preview** | **bool** | Whether previewGrant gives VIEWER access to the subject, whatever the role, until the invitation expires. Omitted leaves it unchanged. | [optional] 

## Example

```python
from tidal.models.resource_grant_invitations_update_operation_payload_data_attributes import ResourceGrantInvitationsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsUpdateOperationPayloadDataAttributes from a JSON string
resource_grant_invitations_update_operation_payload_data_attributes_instance = ResourceGrantInvitationsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
resource_grant_invitations_update_operation_payload_data_attributes_dict = resource_grant_invitations_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of ResourceGrantInvitationsUpdateOperationPayloadDataAttributes from a dict
resource_grant_invitations_update_operation_payload_data_attributes_from_dict = ResourceGrantInvitationsUpdateOperationPayloadDataAttributes.from_dict(resource_grant_invitations_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


