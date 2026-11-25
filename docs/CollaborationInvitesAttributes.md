# CollaborationInvitesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Opaque invite code embedded in the share link | 
**created_at** | **datetime** | Datetime the invite was created (ISO 8601) | 
**expires_at** | **datetime** | Time the invitation expires; accepted grants remain valid | 
**revoked** | **bool** | Whether the invitation has been deleted | 

## Example

```python
from tidal.models.collaboration_invites_attributes import CollaborationInvitesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesAttributes from a JSON string
collaboration_invites_attributes_instance = CollaborationInvitesAttributes.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesAttributes.to_json())

# convert the object into a dict
collaboration_invites_attributes_dict = collaboration_invites_attributes_instance.to_dict()
# create an instance of CollaborationInvitesAttributes from a dict
collaboration_invites_attributes_from_dict = CollaborationInvitesAttributes.from_dict(collaboration_invites_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


