# SquareItemVariationsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artworks** | [**SquareItemVariationsArtworksMultiRelationshipDataDocument**](SquareItemVariationsArtworksMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**SquareItemVariationsOwnersMultiRelationshipDataDocument**](SquareItemVariationsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.square_item_variations_relationships import SquareItemVariationsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsRelationships from a JSON string
square_item_variations_relationships_instance = SquareItemVariationsRelationships.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsRelationships.to_json())

# convert the object into a dict
square_item_variations_relationships_dict = square_item_variations_relationships_instance.to_dict()
# create an instance of SquareItemVariationsRelationships from a dict
square_item_variations_relationships_from_dict = SquareItemVariationsRelationships.from_dict(square_item_variations_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


