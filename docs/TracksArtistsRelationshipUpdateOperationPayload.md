# TracksArtistsRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TracksArtistsRelationshipUpdateOperationPayloadData]**](TracksArtistsRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.tracks_artists_relationship_update_operation_payload import TracksArtistsRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TracksArtistsRelationshipUpdateOperationPayload from a JSON string
tracks_artists_relationship_update_operation_payload_instance = TracksArtistsRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(TracksArtistsRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
tracks_artists_relationship_update_operation_payload_dict = tracks_artists_relationship_update_operation_payload_instance.to_dict()
# create an instance of TracksArtistsRelationshipUpdateOperationPayload from a dict
tracks_artists_relationship_update_operation_payload_from_dict = TracksArtistsRelationshipUpdateOperationPayload.from_dict(tracks_artists_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


