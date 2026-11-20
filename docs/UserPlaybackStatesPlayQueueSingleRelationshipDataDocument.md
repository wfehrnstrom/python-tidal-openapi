# UserPlaybackStatesPlayQueueSingleRelationshipDataDocument

Target resource types: `playQueues`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_playback_states_play_queue_single_relationship_data_document import UserPlaybackStatesPlayQueueSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesPlayQueueSingleRelationshipDataDocument from a JSON string
user_playback_states_play_queue_single_relationship_data_document_instance = UserPlaybackStatesPlayQueueSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesPlayQueueSingleRelationshipDataDocument.to_json())

# convert the object into a dict
user_playback_states_play_queue_single_relationship_data_document_dict = user_playback_states_play_queue_single_relationship_data_document_instance.to_dict()
# create an instance of UserPlaybackStatesPlayQueueSingleRelationshipDataDocument from a dict
user_playback_states_play_queue_single_relationship_data_document_from_dict = UserPlaybackStatesPlayQueueSingleRelationshipDataDocument.from_dict(user_playback_states_play_queue_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


