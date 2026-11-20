# PlaylistsOwnerProfilesMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_owner_profiles_multi_relationship_data_document import PlaylistsOwnerProfilesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsOwnerProfilesMultiRelationshipDataDocument from a JSON string
playlists_owner_profiles_multi_relationship_data_document_instance = PlaylistsOwnerProfilesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsOwnerProfilesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlists_owner_profiles_multi_relationship_data_document_dict = playlists_owner_profiles_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistsOwnerProfilesMultiRelationshipDataDocument from a dict
playlists_owner_profiles_multi_relationship_data_document_from_dict = PlaylistsOwnerProfilesMultiRelationshipDataDocument.from_dict(playlists_owner_profiles_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


