# SquareItemsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artworks** | [**SquareItemsArtworksMultiRelationshipDataDocument**](SquareItemsArtworksMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**SquareItemsOwnersMultiRelationshipDataDocument**](SquareItemsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**variations** | [**SquareItemsVariationsMultiRelationshipDataDocument**](SquareItemsVariationsMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.square_items_relationships import SquareItemsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsRelationships from a JSON string
square_items_relationships_instance = SquareItemsRelationships.from_json(json)
# print the JSON string representation of the object
print(SquareItemsRelationships.to_json())

# convert the object into a dict
square_items_relationships_dict = square_items_relationships_instance.to_dict()
# create an instance of SquareItemsRelationships from a dict
square_items_relationships_from_dict = SquareItemsRelationships.from_dict(square_items_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


