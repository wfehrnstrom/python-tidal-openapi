# UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserPlaybackStatesPlayQueueUpdateResourceIdentifier**](UserPlaybackStatesPlayQueueUpdateResourceIdentifier.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_playback_states_play_queue_update_single_relationship_data_document import UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument from a JSON string
user_playback_states_play_queue_update_single_relationship_data_document_instance = UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument.to_json())

# convert the object into a dict
user_playback_states_play_queue_update_single_relationship_data_document_dict = user_playback_states_play_queue_update_single_relationship_data_document_instance.to_dict()
# create an instance of UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument from a dict
user_playback_states_play_queue_update_single_relationship_data_document_from_dict = UserPlaybackStatesPlayQueueUpdateSingleRelationshipDataDocument.from_dict(user_playback_states_play_queue_update_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


