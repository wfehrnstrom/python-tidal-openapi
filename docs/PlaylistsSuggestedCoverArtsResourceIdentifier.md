# PlaylistsSuggestedCoverArtsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**PlaylistsSuggestedCoverArtsResourceIdentifierMeta**](PlaylistsSuggestedCoverArtsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.playlists_suggested_cover_arts_resource_identifier import PlaylistsSuggestedCoverArtsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsSuggestedCoverArtsResourceIdentifier from a JSON string
playlists_suggested_cover_arts_resource_identifier_instance = PlaylistsSuggestedCoverArtsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(PlaylistsSuggestedCoverArtsResourceIdentifier.to_json())

# convert the object into a dict
playlists_suggested_cover_arts_resource_identifier_dict = playlists_suggested_cover_arts_resource_identifier_instance.to_dict()
# create an instance of PlaylistsSuggestedCoverArtsResourceIdentifier from a dict
playlists_suggested_cover_arts_resource_identifier_from_dict = PlaylistsSuggestedCoverArtsResourceIdentifier.from_dict(playlists_suggested_cover_arts_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


