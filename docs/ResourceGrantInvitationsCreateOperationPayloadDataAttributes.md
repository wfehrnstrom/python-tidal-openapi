# ResourceGrantInvitationsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | Time redemption ends; must be in the future and at most a year away. Defaults to seven days after creation. | [optional] 
**max_uses** | **int** | Number of redemptions permitted, repeated ones included. Unlimited when omitted or null. | [optional] 
**password** | **str** | Password a user must send to redeem. Never returned. Must be printable ASCII characters. Playlist invitations cannot have one; 400. | [optional] 
**preview** | **bool** | Whether previewGrant gives VIEWER access to the subject, whatever the role, until the invitation expires. Defaults to false. | [optional] 
**role** | **str** | Role a redemption grants. | 

## Example

```python
from tidal.models.resource_grant_invitations_create_operation_payload_data_attributes import ResourceGrantInvitationsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsCreateOperationPayloadDataAttributes from a JSON string
resource_grant_invitations_create_operation_payload_data_attributes_instance = ResourceGrantInvitationsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
resource_grant_invitations_create_operation_payload_data_attributes_dict = resource_grant_invitations_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of ResourceGrantInvitationsCreateOperationPayloadDataAttributes from a dict
resource_grant_invitations_create_operation_payload_data_attributes_from_dict = ResourceGrantInvitationsCreateOperationPayloadDataAttributes.from_dict(resource_grant_invitations_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


