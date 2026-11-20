# PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistGenerationsTrackPreferencesRelationshipPayloadData]**](PlaylistGenerationsTrackPreferencesRelationshipPayloadData.md) |  | 
**meta** | [**PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta**](PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta.md) |  | 

## Example

```python
from tidal.models.playlist_generations_track_preferences_relationship_add_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload from a JSON string
playlist_generations_track_preferences_relationship_add_operation_payload_instance = PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload.to_json())

# convert the object into a dict
playlist_generations_track_preferences_relationship_add_operation_payload_dict = playlist_generations_track_preferences_relationship_add_operation_payload_instance.to_dict()
# create an instance of PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload from a dict
playlist_generations_track_preferences_relationship_add_operation_payload_from_dict = PlaylistGenerationsTrackPreferencesRelationshipAddOperationPayload.from_dict(playlist_generations_track_preferences_relationship_add_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


