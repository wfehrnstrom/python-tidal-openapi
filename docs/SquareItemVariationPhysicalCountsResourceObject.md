# SquareItemVariationPhysicalCountsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareItemVariationPhysicalCountsAttributes**](SquareItemVariationPhysicalCountsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.square_item_variation_physical_counts_resource_object import SquareItemVariationPhysicalCountsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationPhysicalCountsResourceObject from a JSON string
square_item_variation_physical_counts_resource_object_instance = SquareItemVariationPhysicalCountsResourceObject.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationPhysicalCountsResourceObject.to_json())

# convert the object into a dict
square_item_variation_physical_counts_resource_object_dict = square_item_variation_physical_counts_resource_object_instance.to_dict()
# create an instance of SquareItemVariationPhysicalCountsResourceObject from a dict
square_item_variation_physical_counts_resource_object_from_dict = SquareItemVariationPhysicalCountsResourceObject.from_dict(square_item_variation_physical_counts_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


