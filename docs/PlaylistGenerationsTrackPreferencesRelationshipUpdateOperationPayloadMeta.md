# PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_preference_version** | **int** |  | 
**mode** | **str** | Relationship mutation mode. INCREMENTAL updates selected existing entries without adding or removing memberships; REPLACE_ALL replaces the complete membership and its order where applicable. Omission defaults to INCREMENTAL. | [optional] [default to 'INCREMENTAL']

## Example

```python
from tidal.models.playlist_generations_track_preferences_relationship_update_operation_payload_meta import PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta from a JSON string
playlist_generations_track_preferences_relationship_update_operation_payload_meta_instance = PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
playlist_generations_track_preferences_relationship_update_operation_payload_meta_dict = playlist_generations_track_preferences_relationship_update_operation_payload_meta_instance.to_dict()
# create an instance of PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta from a dict
playlist_generations_track_preferences_relationship_update_operation_payload_meta_from_dict = PlaylistGenerationsTrackPreferencesRelationshipUpdateOperationPayloadMeta.from_dict(playlist_generations_track_preferences_relationship_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


