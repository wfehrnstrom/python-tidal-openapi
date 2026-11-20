# ResourceGrantInvitationsSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `folders`, `playlists`, `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantInvitationsSubjectResourceIdentifier**](ResourceGrantInvitationsSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grant_invitations_subject_single_relationship_data_document import ResourceGrantInvitationsSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantInvitationsSubjectSingleRelationshipDataDocument from a JSON string
resource_grant_invitations_subject_single_relationship_data_document_instance = ResourceGrantInvitationsSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantInvitationsSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
resource_grant_invitations_subject_single_relationship_data_document_dict = resource_grant_invitations_subject_single_relationship_data_document_instance.to_dict()
# create an instance of ResourceGrantInvitationsSubjectSingleRelationshipDataDocument from a dict
resource_grant_invitations_subject_single_relationship_data_document_from_dict = ResourceGrantInvitationsSubjectSingleRelationshipDataDocument.from_dict(resource_grant_invitations_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


