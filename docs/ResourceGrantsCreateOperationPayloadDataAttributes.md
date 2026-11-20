# ResourceGrantsCreateOperationPayloadDataAttributes

Required for a direct grant; omitted when redeeming.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from tidal.models.resource_grants_create_operation_payload_data_attributes import ResourceGrantsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsCreateOperationPayloadDataAttributes from a JSON string
resource_grants_create_operation_payload_data_attributes_instance = ResourceGrantsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
resource_grants_create_operation_payload_data_attributes_dict = resource_grants_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of ResourceGrantsCreateOperationPayloadDataAttributes from a dict
resource_grants_create_operation_payload_data_attributes_from_dict = ResourceGrantsCreateOperationPayloadDataAttributes.from_dict(resource_grants_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


