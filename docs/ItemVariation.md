# ItemVariation

Variations available for independent catalog edits, in Square's display order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.item_variation import ItemVariation

# TODO update the JSON string below
json = "{}"
# create an instance of ItemVariation from a JSON string
item_variation_instance = ItemVariation.from_json(json)
# print the JSON string representation of the object
print(ItemVariation.to_json())

# convert the object into a dict
item_variation_dict = item_variation_instance.to_dict()
# create an instance of ItemVariation from a dict
item_variation_from_dict = ItemVariation.from_dict(item_variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


