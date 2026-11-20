# SquareItemsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of every price on the item | 
**description** | **str** | Item description | [optional] 
**last_modified_at** | **datetime** | Timestamp when the item was last modified in Square; absent when Square has not reported one | [optional] 
**origin** | **str** | Where the item was created | [optional] 
**published_in_selected_site** | **bool** | Whether the item is published in the seller&#39;s selected Square Online site; false when no site is selected | [optional] 
**revision** | **int** | Square catalog item revision used to guard item updates; excludes inventory stock | 
**title** | **str** | Item title; empty for an untitled item created in Square | 

## Example

```python
from tidal.models.square_items_attributes import SquareItemsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsAttributes from a JSON string
square_items_attributes_instance = SquareItemsAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareItemsAttributes.to_json())

# convert the object into a dict
square_items_attributes_dict = square_items_attributes_instance.to_dict()
# create an instance of SquareItemsAttributes from a dict
square_items_attributes_from_dict = SquareItemsAttributes.from_dict(square_items_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


