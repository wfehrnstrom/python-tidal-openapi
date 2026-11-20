# ClientsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientsResourceObject**](ClientsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.clients_create_single_resource_data_document import ClientsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsCreateSingleResourceDataDocument from a JSON string
clients_create_single_resource_data_document_instance = ClientsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ClientsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
clients_create_single_resource_data_document_dict = clients_create_single_resource_data_document_instance.to_dict()
# create an instance of ClientsCreateSingleResourceDataDocument from a dict
clients_create_single_resource_data_document_from_dict = ClientsCreateSingleResourceDataDocument.from_dict(clients_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


