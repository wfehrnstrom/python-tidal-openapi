# FolderItemsParentSingleRelationshipDataDocument

Target resource types: `folders`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folder_items_parent_single_relationship_data_document import FolderItemsParentSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsParentSingleRelationshipDataDocument from a JSON string
folder_items_parent_single_relationship_data_document_instance = FolderItemsParentSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(FolderItemsParentSingleRelationshipDataDocument.to_json())

# convert the object into a dict
folder_items_parent_single_relationship_data_document_dict = folder_items_parent_single_relationship_data_document_instance.to_dict()
# create an instance of FolderItemsParentSingleRelationshipDataDocument from a dict
folder_items_parent_single_relationship_data_document_from_dict = FolderItemsParentSingleRelationshipDataDocument.from_dict(folder_items_parent_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


