# ClientsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientsResourceObject]**](ClientsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.clients_multi_resource_data_document import ClientsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsMultiResourceDataDocument from a JSON string
clients_multi_resource_data_document_instance = ClientsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ClientsMultiResourceDataDocument.to_json())

# convert the object into a dict
clients_multi_resource_data_document_dict = clients_multi_resource_data_document_instance.to_dict()
# create an instance of ClientsMultiResourceDataDocument from a dict
clients_multi_resource_data_document_from_dict = ClientsMultiResourceDataDocument.from_dict(clients_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


