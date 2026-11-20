# VideosUsageRulesSingleRelationshipDataDocument

Target resource types: `usageRules`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.videos_usage_rules_single_relationship_data_document import VideosUsageRulesSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideosUsageRulesSingleRelationshipDataDocument from a JSON string
videos_usage_rules_single_relationship_data_document_instance = VideosUsageRulesSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideosUsageRulesSingleRelationshipDataDocument.to_json())

# convert the object into a dict
videos_usage_rules_single_relationship_data_document_dict = videos_usage_rules_single_relationship_data_document_instance.to_dict()
# create an instance of VideosUsageRulesSingleRelationshipDataDocument from a dict
videos_usage_rules_single_relationship_data_document_from_dict = VideosUsageRulesSingleRelationshipDataDocument.from_dict(videos_usage_rules_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


