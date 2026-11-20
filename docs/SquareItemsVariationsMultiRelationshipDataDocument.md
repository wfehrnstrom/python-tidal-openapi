# SquareItemsVariationsMultiRelationshipDataDocument

Target resource types: `squareItemVariations`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_items_variations_multi_relationship_data_document import SquareItemsVariationsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemsVariationsMultiRelationshipDataDocument from a JSON string
square_items_variations_multi_relationship_data_document_instance = SquareItemsVariationsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareItemsVariationsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
square_items_variations_multi_relationship_data_document_dict = square_items_variations_multi_relationship_data_document_instance.to_dict()
# create an instance of SquareItemsVariationsMultiRelationshipDataDocument from a dict
square_items_variations_multi_relationship_data_document_from_dict = SquareItemsVariationsMultiRelationshipDataDocument.from_dict(square_items_variations_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


