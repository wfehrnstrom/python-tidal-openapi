# ResourceGrantsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantsCreateOperationPayloadData**](ResourceGrantsCreateOperationPayloadData.md) |  | 
**meta** | [**ResourceGrantsCreateOperationPayloadMeta**](ResourceGrantsCreateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.resource_grants_create_operation_payload import ResourceGrantsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsCreateOperationPayload from a JSON string
resource_grants_create_operation_payload_instance = ResourceGrantsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsCreateOperationPayload.to_json())

# convert the object into a dict
resource_grants_create_operation_payload_dict = resource_grants_create_operation_payload_instance.to_dict()
# create an instance of ResourceGrantsCreateOperationPayload from a dict
resource_grants_create_operation_payload_from_dict = ResourceGrantsCreateOperationPayload.from_dict(resource_grants_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


