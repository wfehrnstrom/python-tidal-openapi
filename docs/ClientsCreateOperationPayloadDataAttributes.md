# ClientsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from tidal.models.clients_create_operation_payload_data_attributes import ClientsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsCreateOperationPayloadDataAttributes from a JSON string
clients_create_operation_payload_data_attributes_instance = ClientsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ClientsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
clients_create_operation_payload_data_attributes_dict = clients_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of ClientsCreateOperationPayloadDataAttributes from a dict
clients_create_operation_payload_data_attributes_from_dict = ClientsCreateOperationPayloadDataAttributes.from_dict(clients_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


