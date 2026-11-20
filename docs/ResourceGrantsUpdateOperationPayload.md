# ResourceGrantsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantsUpdateOperationPayloadData**](ResourceGrantsUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.resource_grants_update_operation_payload import ResourceGrantsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsUpdateOperationPayload from a JSON string
resource_grants_update_operation_payload_instance = ResourceGrantsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsUpdateOperationPayload.to_json())

# convert the object into a dict
resource_grants_update_operation_payload_dict = resource_grants_update_operation_payload_instance.to_dict()
# create an instance of ResourceGrantsUpdateOperationPayload from a dict
resource_grants_update_operation_payload_from_dict = ResourceGrantsUpdateOperationPayload.from_dict(resource_grants_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


