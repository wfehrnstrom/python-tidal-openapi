# ResourceGrantsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceGrantsUpdateOperationPayloadDataAttributes**](ResourceGrantsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.resource_grants_update_operation_payload_data import ResourceGrantsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsUpdateOperationPayloadData from a JSON string
resource_grants_update_operation_payload_data_instance = ResourceGrantsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsUpdateOperationPayloadData.to_json())

# convert the object into a dict
resource_grants_update_operation_payload_data_dict = resource_grants_update_operation_payload_data_instance.to_dict()
# create an instance of ResourceGrantsUpdateOperationPayloadData from a dict
resource_grants_update_operation_payload_data_from_dict = ResourceGrantsUpdateOperationPayloadData.from_dict(resource_grants_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


