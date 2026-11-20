# ClientsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientsCreateOperationPayloadData**](ClientsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.clients_create_operation_payload import ClientsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsCreateOperationPayload from a JSON string
clients_create_operation_payload_instance = ClientsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ClientsCreateOperationPayload.to_json())

# convert the object into a dict
clients_create_operation_payload_dict = clients_create_operation_payload_instance.to_dict()
# create an instance of ClientsCreateOperationPayload from a dict
clients_create_operation_payload_from_dict = ClientsCreateOperationPayload.from_dict(clients_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


