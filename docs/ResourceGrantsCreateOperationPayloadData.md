# ResourceGrantsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceGrantsCreateOperationPayloadDataAttributes**](ResourceGrantsCreateOperationPayloadDataAttributes.md) |  | [optional] 
**relationships** | [**ResourceGrantsCreateOperationPayloadDataRelationships**](ResourceGrantsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.resource_grants_create_operation_payload_data import ResourceGrantsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsCreateOperationPayloadData from a JSON string
resource_grants_create_operation_payload_data_instance = ResourceGrantsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsCreateOperationPayloadData.to_json())

# convert the object into a dict
resource_grants_create_operation_payload_data_dict = resource_grants_create_operation_payload_data_instance.to_dict()
# create an instance of ResourceGrantsCreateOperationPayloadData from a dict
resource_grants_create_operation_payload_data_from_dict = ResourceGrantsCreateOperationPayloadData.from_dict(resource_grants_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


