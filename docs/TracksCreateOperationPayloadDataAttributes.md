# TracksCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | Access type | 
**explicit** | **bool** | Explicit content | [optional] 
**title** | **str** |  | 

## Example

```python
from tidal.models.tracks_create_operation_payload_data_attributes import TracksCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TracksCreateOperationPayloadDataAttributes from a JSON string
tracks_create_operation_payload_data_attributes_instance = TracksCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(TracksCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
tracks_create_operation_payload_data_attributes_dict = tracks_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of TracksCreateOperationPayloadDataAttributes from a dict
tracks_create_operation_payload_data_attributes_from_dict = TracksCreateOperationPayloadDataAttributes.from_dict(tracks_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


