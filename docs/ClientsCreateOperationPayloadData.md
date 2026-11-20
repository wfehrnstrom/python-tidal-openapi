# ClientsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ClientsCreateOperationPayloadDataAttributes**](ClientsCreateOperationPayloadDataAttributes.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.clients_create_operation_payload_data import ClientsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsCreateOperationPayloadData from a JSON string
clients_create_operation_payload_data_instance = ClientsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ClientsCreateOperationPayloadData.to_json())

# convert the object into a dict
clients_create_operation_payload_data_dict = clients_create_operation_payload_data_instance.to_dict()
# create an instance of ClientsCreateOperationPayloadData from a dict
clients_create_operation_payload_data_from_dict = ClientsCreateOperationPayloadData.from_dict(clients_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


