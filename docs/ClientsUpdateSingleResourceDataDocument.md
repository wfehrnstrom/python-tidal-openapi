# ClientsUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientsResourceObject**](ClientsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.clients_update_single_resource_data_document import ClientsUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsUpdateSingleResourceDataDocument from a JSON string
clients_update_single_resource_data_document_instance = ClientsUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ClientsUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
clients_update_single_resource_data_document_dict = clients_update_single_resource_data_document_instance.to_dict()
# create an instance of ClientsUpdateSingleResourceDataDocument from a dict
clients_update_single_resource_data_document_from_dict = ClientsUpdateSingleResourceDataDocument.from_dict(clients_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


