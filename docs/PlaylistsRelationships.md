# PlaylistsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collaborator_profiles** | [**PlaylistsCollaboratorProfilesMultiRelationshipDataDocument**](PlaylistsCollaboratorProfilesMultiRelationshipDataDocument.md) |  | [optional] 
**collaborators** | [**PlaylistsCollaboratorsMultiRelationshipDataDocument**](PlaylistsCollaboratorsMultiRelationshipDataDocument.md) |  | [optional] 
**cover_art** | [**PlaylistsCoverArtMultiRelationshipDataDocument**](PlaylistsCoverArtMultiRelationshipDataDocument.md) |  | [optional] 
**curators** | [**PlaylistsCuratorsMultiRelationshipDataDocument**](PlaylistsCuratorsMultiRelationshipDataDocument.md) |  | [optional] 
**items** | [**PlaylistsItemsMultiRelationshipDataDocument**](PlaylistsItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owner_profiles** | [**PlaylistsOwnerProfilesMultiRelationshipDataDocument**](PlaylistsOwnerProfilesMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**PlaylistsOwnersMultiRelationshipDataDocument**](PlaylistsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**suggested_cover_arts** | [**PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument**](PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.playlists_relationships import PlaylistsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsRelationships from a JSON string
playlists_relationships_instance = PlaylistsRelationships.from_json(json)
# print the JSON string representation of the object
print(PlaylistsRelationships.to_json())

# convert the object into a dict
playlists_relationships_dict = playlists_relationships_instance.to_dict()
# create an instance of PlaylistsRelationships from a dict
playlists_relationships_from_dict = PlaylistsRelationships.from_dict(playlists_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


