# UserOfflineMixesItemsMultiRelationshipDataDocument

Target resource types: `playlists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_offline_mixes_items_multi_relationship_data_document import UserOfflineMixesItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserOfflineMixesItemsMultiRelationshipDataDocument from a JSON string
user_offline_mixes_items_multi_relationship_data_document_instance = UserOfflineMixesItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserOfflineMixesItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_offline_mixes_items_multi_relationship_data_document_dict = user_offline_mixes_items_multi_relationship_data_document_instance.to_dict()
# create an instance of UserOfflineMixesItemsMultiRelationshipDataDocument from a dict
user_offline_mixes_items_multi_relationship_data_document_from_dict = UserOfflineMixesItemsMultiRelationshipDataDocument.from_dict(user_offline_mixes_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


