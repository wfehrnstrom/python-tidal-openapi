# UserPlaybackStatesUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserPlaybackStatesResourceObject**](UserPlaybackStatesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_playback_states_update_single_resource_data_document import UserPlaybackStatesUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesUpdateSingleResourceDataDocument from a JSON string
user_playback_states_update_single_resource_data_document_instance = UserPlaybackStatesUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
user_playback_states_update_single_resource_data_document_dict = user_playback_states_update_single_resource_data_document_instance.to_dict()
# create an instance of UserPlaybackStatesUpdateSingleResourceDataDocument from a dict
user_playback_states_update_single_resource_data_document_from_dict = UserPlaybackStatesUpdateSingleResourceDataDocument.from_dict(user_playback_states_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


