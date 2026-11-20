# TracksAlbumsRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TracksAlbumsRelationshipUpdateOperationPayloadData]**](TracksAlbumsRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.tracks_albums_relationship_update_operation_payload import TracksAlbumsRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TracksAlbumsRelationshipUpdateOperationPayload from a JSON string
tracks_albums_relationship_update_operation_payload_instance = TracksAlbumsRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(TracksAlbumsRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
tracks_albums_relationship_update_operation_payload_dict = tracks_albums_relationship_update_operation_payload_instance.to_dict()
# create an instance of TracksAlbumsRelationshipUpdateOperationPayload from a dict
tracks_albums_relationship_update_operation_payload_from_dict = TracksAlbumsRelationshipUpdateOperationPayload.from_dict(tracks_albums_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


