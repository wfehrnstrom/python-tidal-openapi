# TracksUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TracksUpdateOperationPayloadData**](TracksUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.tracks_update_operation_payload import TracksUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TracksUpdateOperationPayload from a JSON string
tracks_update_operation_payload_instance = TracksUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(TracksUpdateOperationPayload.to_json())

# convert the object into a dict
tracks_update_operation_payload_dict = tracks_update_operation_payload_instance.to_dict()
# create an instance of TracksUpdateOperationPayload from a dict
tracks_update_operation_payload_from_dict = TracksUpdateOperationPayload.from_dict(tracks_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


