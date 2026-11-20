# PlaylistsCollaboratorsMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_collaborators_multi_relationship_data_document import PlaylistsCollaboratorsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCollaboratorsMultiRelationshipDataDocument from a JSON string
playlists_collaborators_multi_relationship_data_document_instance = PlaylistsCollaboratorsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCollaboratorsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlists_collaborators_multi_relationship_data_document_dict = playlists_collaborators_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistsCollaboratorsMultiRelationshipDataDocument from a dict
playlists_collaborators_multi_relationship_data_document_from_dict = PlaylistsCollaboratorsMultiRelationshipDataDocument.from_dict(playlists_collaborators_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


