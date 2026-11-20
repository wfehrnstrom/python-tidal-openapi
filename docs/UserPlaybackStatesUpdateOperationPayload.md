# UserPlaybackStatesUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserPlaybackStatesUpdateOperationPayloadData**](UserPlaybackStatesUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.user_playback_states_update_operation_payload import UserPlaybackStatesUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlaybackStatesUpdateOperationPayload from a JSON string
user_playback_states_update_operation_payload_instance = UserPlaybackStatesUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(UserPlaybackStatesUpdateOperationPayload.to_json())

# convert the object into a dict
user_playback_states_update_operation_payload_dict = user_playback_states_update_operation_payload_instance.to_dict()
# create an instance of UserPlaybackStatesUpdateOperationPayload from a dict
user_playback_states_update_operation_payload_from_dict = UserPlaybackStatesUpdateOperationPayload.from_dict(user_playback_states_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


