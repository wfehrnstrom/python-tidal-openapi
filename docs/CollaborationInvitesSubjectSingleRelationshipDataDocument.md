# CollaborationInvitesSubjectSingleRelationshipDataDocument

Target resource types: `playlists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.collaboration_invites_subject_single_relationship_data_document import CollaborationInvitesSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationInvitesSubjectSingleRelationshipDataDocument from a JSON string
collaboration_invites_subject_single_relationship_data_document_instance = CollaborationInvitesSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CollaborationInvitesSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
collaboration_invites_subject_single_relationship_data_document_dict = collaboration_invites_subject_single_relationship_data_document_instance.to_dict()
# create an instance of CollaborationInvitesSubjectSingleRelationshipDataDocument from a dict
collaboration_invites_subject_single_relationship_data_document_from_dict = CollaborationInvitesSubjectSingleRelationshipDataDocument.from_dict(collaboration_invites_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


