# ResourceGrantsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceGrantsResourceObject]**](ResourceGrantsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grants_multi_resource_data_document import ResourceGrantsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsMultiResourceDataDocument from a JSON string
resource_grants_multi_resource_data_document_instance = ResourceGrantsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsMultiResourceDataDocument.to_json())

# convert the object into a dict
resource_grants_multi_resource_data_document_dict = resource_grants_multi_resource_data_document_instance.to_dict()
# create an instance of ResourceGrantsMultiResourceDataDocument from a dict
resource_grants_multi_resource_data_document_from_dict = ResourceGrantsMultiResourceDataDocument.from_dict(resource_grants_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


