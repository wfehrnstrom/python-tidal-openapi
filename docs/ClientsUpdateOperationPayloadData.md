# ClientsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ClientsUpdateOperationPayloadDataAttributes**](ClientsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.clients_update_operation_payload_data import ClientsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsUpdateOperationPayloadData from a JSON string
clients_update_operation_payload_data_instance = ClientsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ClientsUpdateOperationPayloadData.to_json())

# convert the object into a dict
clients_update_operation_payload_data_dict = clients_update_operation_payload_data_instance.to_dict()
# create an instance of ClientsUpdateOperationPayloadData from a dict
clients_update_operation_payload_data_from_dict = ClientsUpdateOperationPayloadData.from_dict(clients_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


