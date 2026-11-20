# SquareItemVariationsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_item_variations_owners_multi_relationship_data_document import SquareItemVariationsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareItemVariationsOwnersMultiRelationshipDataDocument from a JSON string
square_item_variations_owners_multi_relationship_data_document_instance = SquareItemVariationsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareItemVariationsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
square_item_variations_owners_multi_relationship_data_document_dict = square_item_variations_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of SquareItemVariationsOwnersMultiRelationshipDataDocument from a dict
square_item_variations_owners_multi_relationship_data_document_from_dict = SquareItemVariationsOwnersMultiRelationshipDataDocument.from_dict(square_item_variations_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


