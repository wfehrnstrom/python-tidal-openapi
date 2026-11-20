# ReactionSummariesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**ReactionSummariesSubjectSingleRelationshipDataDocument**](ReactionSummariesSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.reaction_summaries_relationships import ReactionSummariesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionSummariesRelationships from a JSON string
reaction_summaries_relationships_instance = ReactionSummariesRelationships.from_json(json)
# print the JSON string representation of the object
print(ReactionSummariesRelationships.to_json())

# convert the object into a dict
reaction_summaries_relationships_dict = reaction_summaries_relationships_instance.to_dict()
# create an instance of ReactionSummariesRelationships from a dict
reaction_summaries_relationships_from_dict = ReactionSummariesRelationships.from_dict(reaction_summaries_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


