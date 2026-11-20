# TracksCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TracksCreateOperationPayloadDataAttributes**](TracksCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**TracksCreateOperationPayloadDataRelationships**](TracksCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.tracks_create_operation_payload_data import TracksCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of TracksCreateOperationPayloadData from a JSON string
tracks_create_operation_payload_data_instance = TracksCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(TracksCreateOperationPayloadData.to_json())

# convert the object into a dict
tracks_create_operation_payload_data_dict = tracks_create_operation_payload_data_instance.to_dict()
# create an instance of TracksCreateOperationPayloadData from a dict
tracks_create_operation_payload_data_from_dict = TracksCreateOperationPayloadData.from_dict(tracks_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


