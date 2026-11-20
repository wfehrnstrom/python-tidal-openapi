# ReactionSummariesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ReactionSummariesAttributes**](ReactionSummariesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ReactionSummariesRelationships**](ReactionSummariesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.reaction_summaries_resource_object import ReactionSummariesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionSummariesResourceObject from a JSON string
reaction_summaries_resource_object_instance = ReactionSummariesResourceObject.from_json(json)
# print the JSON string representation of the object
print(ReactionSummariesResourceObject.to_json())

# convert the object into a dict
reaction_summaries_resource_object_dict = reaction_summaries_resource_object_instance.to_dict()
# create an instance of ReactionSummariesResourceObject from a dict
reaction_summaries_resource_object_from_dict = ReactionSummariesResourceObject.from_dict(reaction_summaries_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


