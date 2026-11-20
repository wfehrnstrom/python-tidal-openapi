# UserPlaybackStatesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserPlaybackStatesResourceObject**](UserPlaybackStatesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_playback_states_single_resource_data_document import UserPlaybackStatesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesSingleResourceDataDocument from a JSON string
user_playback_states_single_resource_data_document_instance = UserPlaybackStatesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesSingleResourceDataDocument.to_json())

# convert the object into a dict
user_playback_states_single_resource_data_document_dict = user_playback_states_single_resource_data_document_instance.to_dict()
# create an instance of UserPlaybackStatesSingleResourceDataDocument from a dict
user_playback_states_single_resource_data_document_from_dict = UserPlaybackStatesSingleResourceDataDocument.from_dict(user_playback_states_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


