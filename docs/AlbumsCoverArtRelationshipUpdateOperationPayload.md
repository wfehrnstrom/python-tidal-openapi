# AlbumsCoverArtRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlbumsCoverArtRelationshipUpdateOperationPayloadData]**](AlbumsCoverArtRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.albums_cover_art_relationship_update_operation_payload import AlbumsCoverArtRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsCoverArtRelationshipUpdateOperationPayload from a JSON string
albums_cover_art_relationship_update_operation_payload_instance = AlbumsCoverArtRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(AlbumsCoverArtRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
albums_cover_art_relationship_update_operation_payload_dict = albums_cover_art_relationship_update_operation_payload_instance.to_dict()
# create an instance of AlbumsCoverArtRelationshipUpdateOperationPayload from a dict
albums_cover_art_relationship_update_operation_payload_from_dict = AlbumsCoverArtRelationshipUpdateOperationPayload.from_dict(albums_cover_art_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


