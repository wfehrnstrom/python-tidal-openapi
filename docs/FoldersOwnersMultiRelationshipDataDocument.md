# FoldersOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folders_owners_multi_relationship_data_document import FoldersOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersOwnersMultiRelationshipDataDocument from a JSON string
folders_owners_multi_relationship_data_document_instance = FoldersOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(FoldersOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
folders_owners_multi_relationship_data_document_dict = folders_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of FoldersOwnersMultiRelationshipDataDocument from a dict
folders_owners_multi_relationship_data_document_from_dict = FoldersOwnersMultiRelationshipDataDocument.from_dict(folders_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


