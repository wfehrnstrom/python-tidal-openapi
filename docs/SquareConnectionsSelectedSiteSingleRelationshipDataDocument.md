# SquareConnectionsSelectedSiteSingleRelationshipDataDocument

Target resource types: `squareSites`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_connections_selected_site_single_relationship_data_document import SquareConnectionsSelectedSiteSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsSelectedSiteSingleRelationshipDataDocument from a JSON string
square_connections_selected_site_single_relationship_data_document_instance = SquareConnectionsSelectedSiteSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsSelectedSiteSingleRelationshipDataDocument.to_json())

# convert the object into a dict
square_connections_selected_site_single_relationship_data_document_dict = square_connections_selected_site_single_relationship_data_document_instance.to_dict()
# create an instance of SquareConnectionsSelectedSiteSingleRelationshipDataDocument from a dict
square_connections_selected_site_single_relationship_data_document_from_dict = SquareConnectionsSelectedSiteSingleRelationshipDataDocument.from_dict(square_connections_selected_site_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


