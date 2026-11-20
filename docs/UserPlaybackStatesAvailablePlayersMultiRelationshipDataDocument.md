# UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument

Target resource types: `installations`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_playback_states_available_players_multi_relationship_data_document import UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument from a JSON string
user_playback_states_available_players_multi_relationship_data_document_instance = UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_playback_states_available_players_multi_relationship_data_document_dict = user_playback_states_available_players_multi_relationship_data_document_instance.to_dict()
# create an instance of UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument from a dict
user_playback_states_available_players_multi_relationship_data_document_from_dict = UserPlaybackStatesAvailablePlayersMultiRelationshipDataDocument.from_dict(user_playback_states_available_players_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


