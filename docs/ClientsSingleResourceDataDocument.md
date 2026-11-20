# ClientsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientsResourceObject**](ClientsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.clients_single_resource_data_document import ClientsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsSingleResourceDataDocument from a JSON string
clients_single_resource_data_document_instance = ClientsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ClientsSingleResourceDataDocument.to_json())

# convert the object into a dict
clients_single_resource_data_document_dict = clients_single_resource_data_document_instance.to_dict()
# create an instance of ClientsSingleResourceDataDocument from a dict
clients_single_resource_data_document_from_dict = ClientsSingleResourceDataDocument.from_dict(clients_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


