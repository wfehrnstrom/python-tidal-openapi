# FolderItemsBreadcrumbMultiRelationshipDataDocument

Target resource types: `folders`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folder_items_breadcrumb_multi_relationship_data_document import FolderItemsBreadcrumbMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsBreadcrumbMultiRelationshipDataDocument from a JSON string
folder_items_breadcrumb_multi_relationship_data_document_instance = FolderItemsBreadcrumbMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(FolderItemsBreadcrumbMultiRelationshipDataDocument.to_json())

# convert the object into a dict
folder_items_breadcrumb_multi_relationship_data_document_dict = folder_items_breadcrumb_multi_relationship_data_document_instance.to_dict()
# create an instance of FolderItemsBreadcrumbMultiRelationshipDataDocument from a dict
folder_items_breadcrumb_multi_relationship_data_document_from_dict = FolderItemsBreadcrumbMultiRelationshipDataDocument.from_dict(folder_items_breadcrumb_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


