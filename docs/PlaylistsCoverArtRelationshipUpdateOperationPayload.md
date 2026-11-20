# PlaylistsCoverArtRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistsCoverArtRelationshipUpdateOperationPayloadData]**](PlaylistsCoverArtRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.playlists_cover_art_relationship_update_operation_payload import PlaylistsCoverArtRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCoverArtRelationshipUpdateOperationPayload from a JSON string
playlists_cover_art_relationship_update_operation_payload_instance = PlaylistsCoverArtRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCoverArtRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
playlists_cover_art_relationship_update_operation_payload_dict = playlists_cover_art_relationship_update_operation_payload_instance.to_dict()
# create an instance of PlaylistsCoverArtRelationshipUpdateOperationPayload from a dict
playlists_cover_art_relationship_update_operation_payload_from_dict = PlaylistsCoverArtRelationshipUpdateOperationPayload.from_dict(playlists_cover_art_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


