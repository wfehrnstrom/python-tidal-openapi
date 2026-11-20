# ReactionSummariesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReactionSummariesResourceObject]**](ReactionSummariesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.reaction_summaries_multi_resource_data_document import ReactionSummariesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionSummariesMultiResourceDataDocument from a JSON string
reaction_summaries_multi_resource_data_document_instance = ReactionSummariesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ReactionSummariesMultiResourceDataDocument.to_json())

# convert the object into a dict
reaction_summaries_multi_resource_data_document_dict = reaction_summaries_multi_resource_data_document_instance.to_dict()
# create an instance of ReactionSummariesMultiResourceDataDocument from a dict
reaction_summaries_multi_resource_data_document_from_dict = ReactionSummariesMultiResourceDataDocument.from_dict(reaction_summaries_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


