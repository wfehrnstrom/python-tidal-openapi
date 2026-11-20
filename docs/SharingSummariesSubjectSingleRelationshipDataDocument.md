# SharingSummariesSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `folders`, `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SharingSummariesSubjectResourceIdentifier**](SharingSummariesSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.sharing_summaries_subject_single_relationship_data_document import SharingSummariesSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SharingSummariesSubjectSingleRelationshipDataDocument from a JSON string
sharing_summaries_subject_single_relationship_data_document_instance = SharingSummariesSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SharingSummariesSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
sharing_summaries_subject_single_relationship_data_document_dict = sharing_summaries_subject_single_relationship_data_document_instance.to_dict()
# create an instance of SharingSummariesSubjectSingleRelationshipDataDocument from a dict
sharing_summaries_subject_single_relationship_data_document_from_dict = SharingSummariesSubjectSingleRelationshipDataDocument.from_dict(sharing_summaries_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


