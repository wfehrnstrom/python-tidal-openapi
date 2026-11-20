# SquareConnectionsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_site** | [**SquareConnectionsSelectedSiteSingleRelationshipDataDocument**](SquareConnectionsSelectedSiteSingleRelationshipDataDocument.md) |  | [optional] 
**sites** | [**SquareConnectionsSitesMultiRelationshipDataDocument**](SquareConnectionsSitesMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.square_connections_relationships import SquareConnectionsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsRelationships from a JSON string
square_connections_relationships_instance = SquareConnectionsRelationships.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsRelationships.to_json())

# convert the object into a dict
square_connections_relationships_dict = square_connections_relationships_instance.to_dict()
# create an instance of SquareConnectionsRelationships from a dict
square_connections_relationships_from_dict = SquareConnectionsRelationships.from_dict(square_connections_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


