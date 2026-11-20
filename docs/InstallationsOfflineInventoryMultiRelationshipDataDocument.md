# InstallationsOfflineInventoryMultiRelationshipDataDocument

Target resource types: `albums`, `playlists`, `tracks`, `userCollectionTracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstallationsOfflineInventoryResourceIdentifier]**](InstallationsOfflineInventoryResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.installations_offline_inventory_multi_relationship_data_document import InstallationsOfflineInventoryMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsOfflineInventoryMultiRelationshipDataDocument from a JSON string
installations_offline_inventory_multi_relationship_data_document_instance = InstallationsOfflineInventoryMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(InstallationsOfflineInventoryMultiRelationshipDataDocument.to_json())

# convert the object into a dict
installations_offline_inventory_multi_relationship_data_document_dict = installations_offline_inventory_multi_relationship_data_document_instance.to_dict()
# create an instance of InstallationsOfflineInventoryMultiRelationshipDataDocument from a dict
installations_offline_inventory_multi_relationship_data_document_from_dict = InstallationsOfflineInventoryMultiRelationshipDataDocument.from_dict(installations_offline_inventory_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


