# DownloadsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.downloads_owners_multi_relationship_data_document import DownloadsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadsOwnersMultiRelationshipDataDocument from a JSON string
downloads_owners_multi_relationship_data_document_instance = DownloadsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(DownloadsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
downloads_owners_multi_relationship_data_document_dict = downloads_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of DownloadsOwnersMultiRelationshipDataDocument from a dict
downloads_owners_multi_relationship_data_document_from_dict = DownloadsOwnersMultiRelationshipDataDocument.from_dict(downloads_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


