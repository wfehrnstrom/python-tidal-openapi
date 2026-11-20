# ResourceGrantsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantsResourceObject**](ResourceGrantsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grants_single_resource_data_document import ResourceGrantsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsSingleResourceDataDocument from a JSON string
resource_grants_single_resource_data_document_instance = ResourceGrantsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsSingleResourceDataDocument.to_json())

# convert the object into a dict
resource_grants_single_resource_data_document_dict = resource_grants_single_resource_data_document_instance.to_dict()
# create an instance of ResourceGrantsSingleResourceDataDocument from a dict
resource_grants_single_resource_data_document_from_dict = ResourceGrantsSingleResourceDataDocument.from_dict(resource_grants_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


