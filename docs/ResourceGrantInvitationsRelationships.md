# ResourceGrantInvitationsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**ResourceGrantInvitationsOwnersMultiRelationshipDataDocument**](ResourceGrantInvitationsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**preview_grant** | [**ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument**](ResourceGrantInvitationsPreviewGrantSingleRelationshipDataDocument.md) |  | [optional] 
**subject** | [**ResourceGrantInvitationsSubjectSingleRelationshipDataDocument**](ResourceGrantInvitationsSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.resource_grant_invitations_relationships import ResourceGrantInvitationsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsRelationships from a JSON string
resource_grant_invitations_relationships_instance = ResourceGrantInvitationsRelationships.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsRelationships.to_json())

# convert the object into a dict
resource_grant_invitations_relationships_dict = resource_grant_invitations_relationships_instance.to_dict()
# create an instance of ResourceGrantInvitationsRelationships from a dict
resource_grant_invitations_relationships_from_dict = ResourceGrantInvitationsRelationships.from_dict(resource_grant_invitations_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


