# AlbumsUsageRulesSingleRelationshipDataDocument

Target resource types: `usageRules`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_usage_rules_single_relationship_data_document import AlbumsUsageRulesSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsUsageRulesSingleRelationshipDataDocument from a JSON string
albums_usage_rules_single_relationship_data_document_instance = AlbumsUsageRulesSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsUsageRulesSingleRelationshipDataDocument.to_json())

# convert the object into a dict
albums_usage_rules_single_relationship_data_document_dict = albums_usage_rules_single_relationship_data_document_instance.to_dict()
# create an instance of AlbumsUsageRulesSingleRelationshipDataDocument from a dict
albums_usage_rules_single_relationship_data_document_from_dict = AlbumsUsageRulesSingleRelationshipDataDocument.from_dict(albums_usage_rules_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


