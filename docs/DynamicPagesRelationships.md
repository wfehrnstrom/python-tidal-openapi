# DynamicPagesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modules** | [**DynamicPagesModulesMultiRelationshipDataDocument**](DynamicPagesModulesMultiRelationshipDataDocument.md) |  | [optional] 
**subject** | [**DynamicPagesSubjectSingleRelationshipDataDocument**](DynamicPagesSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.dynamic_pages_relationships import DynamicPagesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPagesRelationships from a JSON string
dynamic_pages_relationships_instance = DynamicPagesRelationships.from_json(json)
# print the JSON string representation of the object
print(DynamicPagesRelationships.to_json())

# convert the object into a dict
dynamic_pages_relationships_dict = dynamic_pages_relationships_instance.to_dict()
# create an instance of DynamicPagesRelationships from a dict
dynamic_pages_relationships_from_dict = DynamicPagesRelationships.from_dict(dynamic_pages_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


