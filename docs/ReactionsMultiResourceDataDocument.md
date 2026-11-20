# ReactionsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReactionsResourceObject]**](ReactionsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.reactions_multi_resource_data_document import ReactionsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsMultiResourceDataDocument from a JSON string
reactions_multi_resource_data_document_instance = ReactionsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ReactionsMultiResourceDataDocument.to_json())

# convert the object into a dict
reactions_multi_resource_data_document_dict = reactions_multi_resource_data_document_instance.to_dict()
# create an instance of ReactionsMultiResourceDataDocument from a dict
reactions_multi_resource_data_document_from_dict = ReactionsMultiResourceDataDocument.from_dict(reactions_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


