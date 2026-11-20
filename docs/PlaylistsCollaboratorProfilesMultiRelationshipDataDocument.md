# PlaylistsCollaboratorProfilesMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_collaborator_profiles_multi_relationship_data_document import PlaylistsCollaboratorProfilesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCollaboratorProfilesMultiRelationshipDataDocument from a JSON string
playlists_collaborator_profiles_multi_relationship_data_document_instance = PlaylistsCollaboratorProfilesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCollaboratorProfilesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlists_collaborator_profiles_multi_relationship_data_document_dict = playlists_collaborator_profiles_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistsCollaboratorProfilesMultiRelationshipDataDocument from a dict
playlists_collaborator_profiles_multi_relationship_data_document_from_dict = PlaylistsCollaboratorProfilesMultiRelationshipDataDocument.from_dict(playlists_collaborator_profiles_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


