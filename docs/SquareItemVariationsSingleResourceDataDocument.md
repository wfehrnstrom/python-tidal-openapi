# SquareItemVariationsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareItemVariationsResourceObject**](SquareItemVariationsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_item_variations_single_resource_data_document import SquareItemVariationsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsSingleResourceDataDocument from a JSON string
square_item_variations_single_resource_data_document_instance = SquareItemVariationsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsSingleResourceDataDocument.to_json())

# convert the object into a dict
square_item_variations_single_resource_data_document_dict = square_item_variations_single_resource_data_document_instance.to_dict()
# create an instance of SquareItemVariationsSingleResourceDataDocument from a dict
square_item_variations_single_resource_data_document_from_dict = SquareItemVariationsSingleResourceDataDocument.from_dict(square_item_variations_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


