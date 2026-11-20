# SharesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**SharesOwnersMultiRelationshipDataDocument**](SharesOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**shared_resources** | [**SharesSharedResourcesMultiRelationshipDataDocument**](SharesSharedResourcesMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.shares_relationships import SharesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SharesRelationships from a JSON string
shares_relationships_instance = SharesRelationships.from_json(json)
# print the JSON string representation of the object
print(SharesRelationships.to_json())

# convert the object into a dict
shares_relationships_dict = shares_relationships_instance.to_dict()
# create an instance of SharesRelationships from a dict
shares_relationships_from_dict = SharesRelationships.from_dict(shares_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


