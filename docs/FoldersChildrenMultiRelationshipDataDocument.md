# FoldersChildrenMultiRelationshipDataDocument

Target resource types: `folderItems`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folders_children_multi_relationship_data_document import FoldersChildrenMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersChildrenMultiRelationshipDataDocument from a JSON string
folders_children_multi_relationship_data_document_instance = FoldersChildrenMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(FoldersChildrenMultiRelationshipDataDocument.to_json())

# convert the object into a dict
folders_children_multi_relationship_data_document_dict = folders_children_multi_relationship_data_document_instance.to_dict()
# create an instance of FoldersChildrenMultiRelationshipDataDocument from a dict
folders_children_multi_relationship_data_document_from_dict = FoldersChildrenMultiRelationshipDataDocument.from_dict(folders_children_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


