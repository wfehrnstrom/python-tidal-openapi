# SquareSitesItemsMultiRelationshipDataDocument

Target resource types: `squareItems`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_sites_items_multi_relationship_data_document import SquareSitesItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareSitesItemsMultiRelationshipDataDocument from a JSON string
square_sites_items_multi_relationship_data_document_instance = SquareSitesItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareSitesItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
square_sites_items_multi_relationship_data_document_dict = square_sites_items_multi_relationship_data_document_instance.to_dict()
# create an instance of SquareSitesItemsMultiRelationshipDataDocument from a dict
square_sites_items_multi_relationship_data_document_from_dict = SquareSitesItemsMultiRelationshipDataDocument.from_dict(square_sites_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


