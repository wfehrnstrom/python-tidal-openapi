# SquareItemsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareItemsAttributes**](SquareItemsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SquareItemsRelationships**](SquareItemsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.square_items_resource_object import SquareItemsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsResourceObject from a JSON string
square_items_resource_object_instance = SquareItemsResourceObject.from_json(json)
# print the JSON string representation of the object
print(SquareItemsResourceObject.to_json())

# convert the object into a dict
square_items_resource_object_dict = square_items_resource_object_instance.to_dict()
# create an instance of SquareItemsResourceObject from a dict
square_items_resource_object_from_dict = SquareItemsResourceObject.from_dict(square_items_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


