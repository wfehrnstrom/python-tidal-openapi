# TracksCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TracksCreateOperationPayloadData**](TracksCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.tracks_create_operation_payload import TracksCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TracksCreateOperationPayload from a JSON string
tracks_create_operation_payload_instance = TracksCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(TracksCreateOperationPayload.to_json())

# convert the object into a dict
tracks_create_operation_payload_dict = tracks_create_operation_payload_instance.to_dict()
# create an instance of TracksCreateOperationPayload from a dict
tracks_create_operation_payload_from_dict = TracksCreateOperationPayload.from_dict(tracks_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


