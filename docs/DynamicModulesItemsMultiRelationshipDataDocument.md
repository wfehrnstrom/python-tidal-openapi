# DynamicModulesItemsMultiRelationshipDataDocument

Target resource types: `albums`, `artistStreamsStatistics`, `artists`, `playlists`, `squareItems`, `studioHomeEventTiles`, `studioHomeInsightTiles`, `studioHomeMerchTiles`, `studioHomeMusicTiles`, `tracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DynamicModulesItemsResourceIdentifier]**](DynamicModulesItemsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dynamic_modules_items_multi_relationship_data_document import DynamicModulesItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicModulesItemsMultiRelationshipDataDocument from a JSON string
dynamic_modules_items_multi_relationship_data_document_instance = DynamicModulesItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(DynamicModulesItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
dynamic_modules_items_multi_relationship_data_document_dict = dynamic_modules_items_multi_relationship_data_document_instance.to_dict()
# create an instance of DynamicModulesItemsMultiRelationshipDataDocument from a dict
dynamic_modules_items_multi_relationship_data_document_from_dict = DynamicModulesItemsMultiRelationshipDataDocument.from_dict(dynamic_modules_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


