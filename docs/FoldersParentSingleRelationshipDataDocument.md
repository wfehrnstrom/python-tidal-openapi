# FoldersParentSingleRelationshipDataDocument

Target resource types: `folders`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folders_parent_single_relationship_data_document import FoldersParentSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersParentSingleRelationshipDataDocument from a JSON string
folders_parent_single_relationship_data_document_instance = FoldersParentSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(FoldersParentSingleRelationshipDataDocument.to_json())

# convert the object into a dict
folders_parent_single_relationship_data_document_dict = folders_parent_single_relationship_data_document_instance.to_dict()
# create an instance of FoldersParentSingleRelationshipDataDocument from a dict
folders_parent_single_relationship_data_document_from_dict = FoldersParentSingleRelationshipDataDocument.from_dict(folders_parent_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


