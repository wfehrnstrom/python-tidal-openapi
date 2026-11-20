# TrackSourceFilesCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TrackSourceFilesCreateOperationPayloadDataAttributes**](TrackSourceFilesCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**TrackSourceFilesCreateOperationPayloadDataRelationships**](TrackSourceFilesCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.track_source_files_create_operation_payload_data import TrackSourceFilesCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesCreateOperationPayloadData from a JSON string
track_source_files_create_operation_payload_data_instance = TrackSourceFilesCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesCreateOperationPayloadData.to_json())

# convert the object into a dict
track_source_files_create_operation_payload_data_dict = track_source_files_create_operation_payload_data_instance.to_dict()
# create an instance of TrackSourceFilesCreateOperationPayloadData from a dict
track_source_files_create_operation_payload_data_from_dict = TrackSourceFilesCreateOperationPayloadData.from_dict(track_source_files_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


