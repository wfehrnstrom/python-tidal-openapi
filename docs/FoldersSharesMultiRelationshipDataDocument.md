# FoldersSharesMultiRelationshipDataDocument

Target resource types: `shares`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.folders_shares_multi_relationship_data_document import FoldersSharesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersSharesMultiRelationshipDataDocument from a JSON string
folders_shares_multi_relationship_data_document_instance = FoldersSharesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(FoldersSharesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
folders_shares_multi_relationship_data_document_dict = folders_shares_multi_relationship_data_document_instance.to_dict()
# create an instance of FoldersSharesMultiRelationshipDataDocument from a dict
folders_shares_multi_relationship_data_document_from_dict = FoldersSharesMultiRelationshipDataDocument.from_dict(folders_shares_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


