# LyricsCreateOperationPayloadDataRelationshipsTrack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LyricsCreateOperationPayloadDataRelationshipsTrackData**](LyricsCreateOperationPayloadDataRelationshipsTrackData.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from tidal.models.lyrics_create_operation_payload_data_relationships_track import LyricsCreateOperationPayloadDataRelationshipsTrack

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsCreateOperationPayloadDataRelationshipsTrack from a JSON string
lyrics_create_operation_payload_data_relationships_track_instance = LyricsCreateOperationPayloadDataRelationshipsTrack.from_json(json)
# print the JSON string representation of the object
print(LyricsCreateOperationPayloadDataRelationshipsTrack.to_json())

# convert the object into a dict
lyrics_create_operation_payload_data_relationships_track_dict = lyrics_create_operation_payload_data_relationships_track_instance.to_dict()
# create an instance of LyricsCreateOperationPayloadDataRelationshipsTrack from a dict
lyrics_create_operation_payload_data_relationships_track_from_dict = LyricsCreateOperationPayloadDataRelationshipsTrack.from_dict(lyrics_create_operation_payload_data_relationships_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


