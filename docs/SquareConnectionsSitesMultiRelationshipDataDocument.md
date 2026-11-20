# SquareConnectionsSitesMultiRelationshipDataDocument

Target resource types: `squareSites`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_connections_sites_multi_relationship_data_document import SquareConnectionsSitesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsSitesMultiRelationshipDataDocument from a JSON string
square_connections_sites_multi_relationship_data_document_instance = SquareConnectionsSitesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsSitesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
square_connections_sites_multi_relationship_data_document_dict = square_connections_sites_multi_relationship_data_document_instance.to_dict()
# create an instance of SquareConnectionsSitesMultiRelationshipDataDocument from a dict
square_connections_sites_multi_relationship_data_document_from_dict = SquareConnectionsSitesMultiRelationshipDataDocument.from_dict(square_connections_sites_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


