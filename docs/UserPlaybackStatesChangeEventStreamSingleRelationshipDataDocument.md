# UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument

Target resource types: `changeEventStreams`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_playback_states_change_event_stream_single_relationship_data_document import UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument from a JSON string
user_playback_states_change_event_stream_single_relationship_data_document_instance = UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument.to_json())

# convert the object into a dict
user_playback_states_change_event_stream_single_relationship_data_document_dict = user_playback_states_change_event_stream_single_relationship_data_document_instance.to_dict()
# create an instance of UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument from a dict
user_playback_states_change_event_stream_single_relationship_data_document_from_dict = UserPlaybackStatesChangeEventStreamSingleRelationshipDataDocument.from_dict(user_playback_states_change_event_stream_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


