# ClientsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_preset** | **str** | Client preset defining default OAuth settings and supported audio formats. | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from tidal.models.clients_update_operation_payload_data_attributes import ClientsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsUpdateOperationPayloadDataAttributes from a JSON string
clients_update_operation_payload_data_attributes_instance = ClientsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ClientsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
clients_update_operation_payload_data_attributes_dict = clients_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of ClientsUpdateOperationPayloadDataAttributes from a dict
clients_update_operation_payload_data_attributes_from_dict = ClientsUpdateOperationPayloadDataAttributes.from_dict(clients_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


