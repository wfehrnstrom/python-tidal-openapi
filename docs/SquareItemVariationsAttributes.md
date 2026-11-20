# SquareItemVariationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**name** | **str** | Variation name; may be empty | 
**price** | **str** | Amount in the currency&#39;s major units | [optional] 
**pricing_type** | **str** | Effective pricing mode at the selected site&#39;s shipping location (merchant-main fallback). Price is present only for FIXED when its amount is available | 
**revision** | **int** | Square variation revision covering its catalog fields, including name, pricing, stock tracking and attached artworks; excludes inventory quantity and other variations | 
**stock_quantity** | **int** | Units at the selected site&#39;s shipping location (merchant-main fallback); present only when tracked and available; may be negative | [optional] 
**stock_tracked** | **bool** | Whether Square tracks stock at the selected site&#39;s shipping location (merchant-main fallback) | 

## Example

```python
from tidal.models.square_item_variations_attributes import SquareItemVariationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsAttributes from a JSON string
square_item_variations_attributes_instance = SquareItemVariationsAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsAttributes.to_json())

# convert the object into a dict
square_item_variations_attributes_dict = square_item_variations_attributes_instance.to_dict()
# create an instance of SquareItemVariationsAttributes from a dict
square_item_variations_attributes_from_dict = SquareItemVariationsAttributes.from_dict(square_item_variations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


