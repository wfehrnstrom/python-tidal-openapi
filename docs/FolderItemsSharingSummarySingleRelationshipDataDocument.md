# FolderItemsSharingSummarySingleRelationshipDataDocument

Target resource types: `sharingSummaries`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folder_items_sharing_summary_single_relationship_data_document import FolderItemsSharingSummarySingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsSharingSummarySingleRelationshipDataDocument from a JSON string
folder_items_sharing_summary_single_relationship_data_document_instance = FolderItemsSharingSummarySingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(FolderItemsSharingSummarySingleRelationshipDataDocument.to_json())

# convert the object into a dict
folder_items_sharing_summary_single_relationship_data_document_dict = folder_items_sharing_summary_single_relationship_data_document_instance.to_dict()
# create an instance of FolderItemsSharingSummarySingleRelationshipDataDocument from a dict
folder_items_sharing_summary_single_relationship_data_document_from_dict = FolderItemsSharingSummarySingleRelationshipDataDocument.from_dict(folder_items_sharing_summary_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


