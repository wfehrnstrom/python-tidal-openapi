# SquareItemVariationsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareItemVariationsAttributes**](SquareItemVariationsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SquareItemVariationsRelationships**](SquareItemVariationsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.square_item_variations_resource_object import SquareItemVariationsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsResourceObject from a JSON string
square_item_variations_resource_object_instance = SquareItemVariationsResourceObject.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsResourceObject.to_json())

# convert the object into a dict
square_item_variations_resource_object_dict = square_item_variations_resource_object_instance.to_dict()
# create an instance of SquareItemVariationsResourceObject from a dict
square_item_variations_resource_object_from_dict = SquareItemVariationsResourceObject.from_dict(square_item_variations_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


