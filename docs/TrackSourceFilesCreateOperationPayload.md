# TrackSourceFilesCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrackSourceFilesCreateOperationPayloadData**](TrackSourceFilesCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.track_source_files_create_operation_payload import TrackSourceFilesCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesCreateOperationPayload from a JSON string
track_source_files_create_operation_payload_instance = TrackSourceFilesCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesCreateOperationPayload.to_json())

# convert the object into a dict
track_source_files_create_operation_payload_dict = track_source_files_create_operation_payload_instance.to_dict()
# create an instance of TrackSourceFilesCreateOperationPayload from a dict
track_source_files_create_operation_payload_from_dict = TrackSourceFilesCreateOperationPayload.from_dict(track_source_files_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


