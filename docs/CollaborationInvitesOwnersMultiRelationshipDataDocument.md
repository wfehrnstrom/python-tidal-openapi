# CollaborationInvitesOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.collaboration_invites_owners_multi_relationship_data_document import CollaborationInvitesOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesOwnersMultiRelationshipDataDocument from a JSON string
collaboration_invites_owners_multi_relationship_data_document_instance = CollaborationInvitesOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
collaboration_invites_owners_multi_relationship_data_document_dict = collaboration_invites_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of CollaborationInvitesOwnersMultiRelationshipDataDocument from a dict
collaboration_invites_owners_multi_relationship_data_document_from_dict = CollaborationInvitesOwnersMultiRelationshipDataDocument.from_dict(collaboration_invites_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


