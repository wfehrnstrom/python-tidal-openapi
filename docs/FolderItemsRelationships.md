# FolderItemsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breadcrumb** | [**FolderItemsBreadcrumbMultiRelationshipDataDocument**](FolderItemsBreadcrumbMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**FolderItemsOwnersMultiRelationshipDataDocument**](FolderItemsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**parent** | [**FolderItemsParentSingleRelationshipDataDocument**](FolderItemsParentSingleRelationshipDataDocument.md) |  | [optional] 
**sharing_summary** | [**FolderItemsSharingSummarySingleRelationshipDataDocument**](FolderItemsSharingSummarySingleRelationshipDataDocument.md) |  | [optional] 
**subject** | [**FolderItemsSubjectSingleRelationshipDataDocument**](FolderItemsSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.folder_items_relationships import FolderItemsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsRelationships from a JSON string
folder_items_relationships_instance = FolderItemsRelationships.from_json(json)
# print the JSON string representation of the object
print(FolderItemsRelationships.to_json())

# convert the object into a dict
folder_items_relationships_dict = folder_items_relationships_instance.to_dict()
# create an instance of FolderItemsRelationships from a dict
folder_items_relationships_from_dict = FolderItemsRelationships.from_dict(folder_items_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


