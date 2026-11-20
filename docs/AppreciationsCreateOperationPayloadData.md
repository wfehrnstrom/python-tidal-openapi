# AppreciationsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | [**AppreciationsCreateOperationPayloadDataRelationships**](AppreciationsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.appreciations_create_operation_payload_data import AppreciationsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of AppreciationsCreateOperationPayloadData from a JSON string
appreciations_create_operation_payload_data_instance = AppreciationsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(AppreciationsCreateOperationPayloadData.to_json())

# convert the object into a dict
appreciations_create_operation_payload_data_dict = appreciations_create_operation_payload_data_instance.to_dict()
# create an instance of AppreciationsCreateOperationPayloadData from a dict
appreciations_create_operation_payload_data_from_dict = AppreciationsCreateOperationPayloadData.from_dict(appreciations_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


