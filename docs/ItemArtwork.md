# ItemArtwork

Item photos in Square's display order, including photos without an available URL; the first is the primary photo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.item_artwork import ItemArtwork

# TODO update the JSON string below
json = "{}"
# create an instance of ItemArtwork from a JSON string
item_artwork_instance = ItemArtwork.from_json(json)
# print the JSON string representation of the object
print(ItemArtwork.to_json())

# convert the object into a dict
item_artwork_dict = item_artwork_instance.to_dict()
# create an instance of ItemArtwork from a dict
item_artwork_from_dict = ItemArtwork.from_dict(item_artwork_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


