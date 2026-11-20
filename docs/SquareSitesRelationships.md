# SquareSitesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**SquareSitesItemsMultiRelationshipDataDocument**](SquareSitesItemsMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.square_sites_relationships import SquareSitesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SquareSitesRelationships from a JSON string
square_sites_relationships_instance = SquareSitesRelationships.from_json(json)
# print the JSON string representation of the object
print(SquareSitesRelationships.to_json())

# convert the object into a dict
square_sites_relationships_dict = square_sites_relationships_instance.to_dict()
# create an instance of SquareSitesRelationships from a dict
square_sites_relationships_from_dict = SquareSitesRelationships.from_dict(square_sites_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


