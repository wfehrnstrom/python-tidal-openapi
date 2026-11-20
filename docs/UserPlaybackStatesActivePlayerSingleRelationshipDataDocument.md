# UserPlaybackStatesActivePlayerSingleRelationshipDataDocument

Target resource types: `installations`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_playback_states_active_player_single_relationship_data_document import UserPlaybackStatesActivePlayerSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesActivePlayerSingleRelationshipDataDocument from a JSON string
user_playback_states_active_player_single_relationship_data_document_instance = UserPlaybackStatesActivePlayerSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesActivePlayerSingleRelationshipDataDocument.to_json())

# convert the object into a dict
user_playback_states_active_player_single_relationship_data_document_dict = user_playback_states_active_player_single_relationship_data_document_instance.to_dict()
# create an instance of UserPlaybackStatesActivePlayerSingleRelationshipDataDocument from a dict
user_playback_states_active_player_single_relationship_data_document_from_dict = UserPlaybackStatesActivePlayerSingleRelationshipDataDocument.from_dict(user_playback_states_active_player_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


