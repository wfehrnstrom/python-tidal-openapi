# SquareItemVariationPhysicalCountsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurred_at** | **datetime** |  | 
**quantity** | **int** |  | 
**square_location_id** | **str** | Square location where this physical count was recorded | 

## Example

```python
from tidal.models.square_item_variation_physical_counts_attributes import SquareItemVariationPhysicalCountsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationPhysicalCountsAttributes from a JSON string
square_item_variation_physical_counts_attributes_instance = SquareItemVariationPhysicalCountsAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationPhysicalCountsAttributes.to_json())

# convert the object into a dict
square_item_variation_physical_counts_attributes_dict = square_item_variation_physical_counts_attributes_instance.to_dict()
# create an instance of SquareItemVariationPhysicalCountsAttributes from a dict
square_item_variation_physical_counts_attributes_from_dict = SquareItemVariationPhysicalCountsAttributes.from_dict(square_item_variation_physical_counts_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


