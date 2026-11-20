# ClientsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientsUpdateOperationPayloadData**](ClientsUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.clients_update_operation_payload import ClientsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsUpdateOperationPayload from a JSON string
clients_update_operation_payload_instance = ClientsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ClientsUpdateOperationPayload.to_json())

# convert the object into a dict
clients_update_operation_payload_dict = clients_update_operation_payload_instance.to_dict()
# create an instance of ClientsUpdateOperationPayload from a dict
clients_update_operation_payload_from_dict = ClientsUpdateOperationPayload.from_dict(clients_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


