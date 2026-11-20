# UserPlaybackStatesUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserPlaybackStatesUpdateOperationPayloadDataAttributes**](UserPlaybackStatesUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** | Also accepts &#x60;me&#x60;. | 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_playback_states_update_operation_payload_data import UserPlaybackStatesUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesUpdateOperationPayloadData from a JSON string
user_playback_states_update_operation_payload_data_instance = UserPlaybackStatesUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesUpdateOperationPayloadData.to_json())

# convert the object into a dict
user_playback_states_update_operation_payload_data_dict = user_playback_states_update_operation_payload_data_instance.to_dict()
# create an instance of UserPlaybackStatesUpdateOperationPayloadData from a dict
user_playback_states_update_operation_payload_data_from_dict = UserPlaybackStatesUpdateOperationPayloadData.from_dict(user_playback_states_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


