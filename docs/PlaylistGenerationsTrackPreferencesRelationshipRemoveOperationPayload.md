# PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayloadData]**](PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayloadData.md) |  | 
**meta** | [**PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta**](PlaylistGenerationsTrackPreferencesRelationshipPayloadMeta.md) |  | 

## Example

```python
from tidal.models.playlist_generations_track_preferences_relationship_remove_operation_payload import PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload from a JSON string
playlist_generations_track_preferences_relationship_remove_operation_payload_instance = PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload.to_json())

# convert the object into a dict
playlist_generations_track_preferences_relationship_remove_operation_payload_dict = playlist_generations_track_preferences_relationship_remove_operation_payload_instance.to_dict()
# create an instance of PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload from a dict
playlist_generations_track_preferences_relationship_remove_operation_payload_from_dict = PlaylistGenerationsTrackPreferencesRelationshipRemoveOperationPayload.from_dict(playlist_generations_track_preferences_relationship_remove_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


