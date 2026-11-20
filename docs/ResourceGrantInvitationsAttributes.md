# ResourceGrantInvitationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code that identifies the invitation to its recipients. | 
**created_at** | **datetime** | Time the invitation was created. | 
**expires_at** | **datetime** | Time redemption ends; issued grants remain. | 
**max_uses** | **int** | Number of redemptions permitted. Absent when unlimited. | [optional] 
**password** | **str** | Password a user must send to redeem. Write-only: never returned. | [optional] 
**password_protected** | **bool** | Whether redemption requires a password. Only the owner and users with a role on the subject see a protected invitation&#39;s subject; others get null linkage. | 
**preview** | **bool** | Whether previewGrant gives VIEWER access to the subject until the invitation expires. | 
**redemption_link** | [**LinkObject**](LinkObject.md) |  | [optional] 
**role** | **str** | Role a redemption grants. | 
**use_count** | **int** | Number of redemptions so far, repeated ones included. Absent when maxUses is. | [optional] 

## Example

```python
from tidal.models.resource_grant_invitations_attributes import ResourceGrantInvitationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsAttributes from a JSON string
resource_grant_invitations_attributes_instance = ResourceGrantInvitationsAttributes.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsAttributes.to_json())

# convert the object into a dict
resource_grant_invitations_attributes_dict = resource_grant_invitations_attributes_instance.to_dict()
# create an instance of ResourceGrantInvitationsAttributes from a dict
resource_grant_invitations_attributes_from_dict = ResourceGrantInvitationsAttributes.from_dict(resource_grant_invitations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


