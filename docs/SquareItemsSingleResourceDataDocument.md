# SquareItemsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareItemsResourceObject**](SquareItemsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_items_single_resource_data_document import SquareItemsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsSingleResourceDataDocument from a JSON string
square_items_single_resource_data_document_instance = SquareItemsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareItemsSingleResourceDataDocument.to_json())

# convert the object into a dict
square_items_single_resource_data_document_dict = square_items_single_resource_data_document_instance.to_dict()
# create an instance of SquareItemsSingleResourceDataDocument from a dict
square_items_single_resource_data_document_from_dict = SquareItemsSingleResourceDataDocument.from_dict(square_items_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


