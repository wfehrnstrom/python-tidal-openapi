# AlbumsArtistsRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlbumsArtistsRelationshipUpdateOperationPayloadData]**](AlbumsArtistsRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.albums_artists_relationship_update_operation_payload import AlbumsArtistsRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsArtistsRelationshipUpdateOperationPayload from a JSON string
albums_artists_relationship_update_operation_payload_instance = AlbumsArtistsRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(AlbumsArtistsRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
albums_artists_relationship_update_operation_payload_dict = albums_artists_relationship_update_operation_payload_instance.to_dict()
# create an instance of AlbumsArtistsRelationshipUpdateOperationPayload from a dict
albums_artists_relationship_update_operation_payload_from_dict = AlbumsArtistsRelationshipUpdateOperationPayload.from_dict(albums_artists_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


