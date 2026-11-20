# AppreciationsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AppreciationsCreateOperationPayloadData**](AppreciationsCreateOperationPayloadData.md) |  | 
**meta** | [**AppreciationsCreateOperationPayloadMeta**](AppreciationsCreateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.appreciations_create_operation_payload import AppreciationsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AppreciationsCreateOperationPayload from a JSON string
appreciations_create_operation_payload_instance = AppreciationsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(AppreciationsCreateOperationPayload.to_json())

# convert the object into a dict
appreciations_create_operation_payload_dict = appreciations_create_operation_payload_instance.to_dict()
# create an instance of AppreciationsCreateOperationPayload from a dict
appreciations_create_operation_payload_from_dict = AppreciationsCreateOperationPayload.from_dict(appreciations_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


