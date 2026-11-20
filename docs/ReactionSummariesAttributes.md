# ReactionSummariesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts_by_emoji** | **Dict[str, int]** | Complete reaction counts keyed by emoji for source files and comments. An empty object means no reactions. | 
**total_count** | **int** | Number of current reactions across all emojis and time offsets, including whole-subject reactions. A user can contribute more than one reaction. | 

## Example

```python
from tidal.models.reaction_summaries_attributes import ReactionSummariesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionSummariesAttributes from a JSON string
reaction_summaries_attributes_instance = ReactionSummariesAttributes.from_json(json)
# print the JSON string representation of the object
print(ReactionSummariesAttributes.to_json())

# convert the object into a dict
reaction_summaries_attributes_dict = reaction_summaries_attributes_instance.to_dict()
# create an instance of ReactionSummariesAttributes from a dict
reaction_summaries_attributes_from_dict = ReactionSummariesAttributes.from_dict(reaction_summaries_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


