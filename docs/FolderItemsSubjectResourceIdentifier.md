# FolderItemsSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**FolderItemsSubjectResourceIdentifierMeta**](FolderItemsSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.folder_items_subject_resource_identifier import FolderItemsSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsSubjectResourceIdentifier from a JSON string
folder_items_subject_resource_identifier_instance = FolderItemsSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(FolderItemsSubjectResourceIdentifier.to_json())

# convert the object into a dict
folder_items_subject_resource_identifier_dict = folder_items_subject_resource_identifier_instance.to_dict()
# create an instance of FolderItemsSubjectResourceIdentifier from a dict
folder_items_subject_resource_identifier_from_dict = FolderItemsSubjectResourceIdentifier.from_dict(folder_items_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


