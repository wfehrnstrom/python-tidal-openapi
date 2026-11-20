# DynamicPagesSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `artists`, `playlists`, `tracks`, `users`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DynamicPagesSubjectResourceIdentifier**](DynamicPagesSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dynamic_pages_subject_single_relationship_data_document import DynamicPagesSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPagesSubjectSingleRelationshipDataDocument from a JSON string
dynamic_pages_subject_single_relationship_data_document_instance = DynamicPagesSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(DynamicPagesSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
dynamic_pages_subject_single_relationship_data_document_dict = dynamic_pages_subject_single_relationship_data_document_instance.to_dict()
# create an instance of DynamicPagesSubjectSingleRelationshipDataDocument from a dict
dynamic_pages_subject_single_relationship_data_document_from_dict = DynamicPagesSubjectSingleRelationshipDataDocument.from_dict(dynamic_pages_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


