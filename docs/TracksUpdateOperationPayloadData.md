# TracksUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TracksUpdateOperationPayloadDataAttributes**](TracksUpdateOperationPayloadDataAttributes.md) |  | [optional] 
**id** | **str** |  | 
**relationships** | [**TracksUpdateOperationPayloadDataRelationships**](TracksUpdateOperationPayloadDataRelationships.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.tracks_update_operation_payload_data import TracksUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of TracksUpdateOperationPayloadData from a JSON string
tracks_update_operation_payload_data_instance = TracksUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(TracksUpdateOperationPayloadData.to_json())

# convert the object into a dict
tracks_update_operation_payload_data_dict = tracks_update_operation_payload_data_instance.to_dict()
# create an instance of TracksUpdateOperationPayloadData from a dict
tracks_update_operation_payload_data_from_dict = TracksUpdateOperationPayloadData.from_dict(tracks_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


