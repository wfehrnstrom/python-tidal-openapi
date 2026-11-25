# FoldersRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**FoldersChildrenMultiRelationshipDataDocument**](FoldersChildrenMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**FoldersOwnersMultiRelationshipDataDocument**](FoldersOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**parent** | [**FoldersParentSingleRelationshipDataDocument**](FoldersParentSingleRelationshipDataDocument.md) |  | [optional] 
**preview** | [**FoldersPreviewMultiRelationshipDataDocument**](FoldersPreviewMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.folders_relationships import FoldersRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersRelationships from a JSON string
folders_relationships_instance = FoldersRelationships.from_json(json)
# print the JSON string representation of the object
print(FoldersRelationships.to_json())

# convert the object into a dict
folders_relationships_dict = folders_relationships_instance.to_dict()
# create an instance of FoldersRelationships from a dict
folders_relationships_from_dict = FoldersRelationships.from_dict(folders_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


