# SquareItemsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SquareItemsResourceObject]**](SquareItemsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_items_multi_resource_data_document import SquareItemsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsMultiResourceDataDocument from a JSON string
square_items_multi_resource_data_document_instance = SquareItemsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareItemsMultiResourceDataDocument.to_json())

# convert the object into a dict
square_items_multi_resource_data_document_dict = square_items_multi_resource_data_document_instance.to_dict()
# create an instance of SquareItemsMultiResourceDataDocument from a dict
square_items_multi_resource_data_document_from_dict = SquareItemsMultiResourceDataDocument.from_dict(square_items_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


