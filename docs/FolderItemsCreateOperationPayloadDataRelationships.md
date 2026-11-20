# FolderItemsCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**FolderItemsCreateOperationPayloadDataRelationshipsParent**](FolderItemsCreateOperationPayloadDataRelationshipsParent.md) |  | 
**subject** | [**FolderItemsCreateOperationPayloadDataRelationshipsSubject**](FolderItemsCreateOperationPayloadDataRelationshipsSubject.md) |  | 

## Example

```python
from tidal.models.folder_items_create_operation_payload_data_relationships import FolderItemsCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsCreateOperationPayloadDataRelationships from a JSON string
folder_items_create_operation_payload_data_relationships_instance = FolderItemsCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(FolderItemsCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
folder_items_create_operation_payload_data_relationships_dict = folder_items_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of FolderItemsCreateOperationPayloadDataRelationships from a dict
folder_items_create_operation_payload_data_relationships_from_dict = FolderItemsCreateOperationPayloadDataRelationships.from_dict(folder_items_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


