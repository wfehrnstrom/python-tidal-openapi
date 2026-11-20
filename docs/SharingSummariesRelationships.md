# SharingSummariesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**SharingSummariesSubjectSingleRelationshipDataDocument**](SharingSummariesSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.sharing_summaries_relationships import SharingSummariesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SharingSummariesRelationships from a JSON string
sharing_summaries_relationships_instance = SharingSummariesRelationships.from_json(json)
# print the JSON string representation of the object
print(SharingSummariesRelationships.to_json())

# convert the object into a dict
sharing_summaries_relationships_dict = sharing_summaries_relationships_instance.to_dict()
# create an instance of SharingSummariesRelationships from a dict
sharing_summaries_relationships_from_dict = SharingSummariesRelationships.from_dict(sharing_summaries_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


