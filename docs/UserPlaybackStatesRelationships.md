# UserPlaybackStatesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_player** | [**UserPlaybackStatesActivePlayerSingleRelationshipDataDocument**](UserPlaybackStatesActivePlayerSingleRelationshipDataDocument.md) |  | [optional] 
**available_players** | [**UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument**](UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument.md) |  | [optional] 
**change_event_stream** | [**UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument**](UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument.md) |  | [optional] 
**play_queue** | [**UserPlaybackStatesPlayQueueSingleRelationshipDataDocument**](UserPlaybackStatesPlayQueueSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_playback_states_relationships import UserPlaybackStatesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesRelationships from a JSON string
user_playback_states_relationships_instance = UserPlaybackStatesRelationships.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesRelationships.to_json())

# convert the object into a dict
user_playback_states_relationships_dict = user_playback_states_relationships_instance.to_dict()
# create an instance of UserPlaybackStatesRelationships from a dict
user_playback_states_relationships_from_dict = UserPlaybackStatesRelationships.from_dict(user_playback_states_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


