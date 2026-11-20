# FolderItemsSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `folders`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FolderItemsSubjectResourceIdentifier**](FolderItemsSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folder_items_subject_single_relationship_data_document import FolderItemsSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsSubjectSingleRelationshipDataDocument from a JSON string
folder_items_subject_single_relationship_data_document_instance = FolderItemsSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(FolderItemsSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
folder_items_subject_single_relationship_data_document_dict = folder_items_subject_single_relationship_data_document_instance.to_dict()
# create an instance of FolderItemsSubjectSingleRelationshipDataDocument from a dict
folder_items_subject_single_relationship_data_document_from_dict = FolderItemsSubjectSingleRelationshipDataDocument.from_dict(folder_items_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


