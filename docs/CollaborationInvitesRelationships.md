# CollaborationInvitesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**CollaborationInvitesOwnersMultiRelationshipDataDocument**](CollaborationInvitesOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**subject** | [**CollaborationInvitesSubjectSingleRelationshipDataDocument**](CollaborationInvitesSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.collaboration_invites_relationships import CollaborationInvitesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesRelationships from a JSON string
collaboration_invites_relationships_instance = CollaborationInvitesRelationships.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesRelationships.to_json())

# convert the object into a dict
collaboration_invites_relationships_dict = collaboration_invites_relationships_instance.to_dict()
# create an instance of CollaborationInvitesRelationships from a dict
collaboration_invites_relationships_from_dict = CollaborationInvitesRelationships.from_dict(collaboration_invites_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


