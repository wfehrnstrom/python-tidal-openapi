# UserDiscoveryMixesItemsMultiRelationshipDataDocument

Target resource types: `playlists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_discovery_mixes_items_multi_relationship_data_document import UserDiscoveryMixesItemsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserDiscoveryMixesItemsMultiRelationshipDataDocument from a JSON string
user_discovery_mixes_items_multi_relationship_data_document_instance = UserDiscoveryMixesItemsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserDiscoveryMixesItemsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_discovery_mixes_items_multi_relationship_data_document_dict = user_discovery_mixes_items_multi_relationship_data_document_instance.to_dict()
# create an instance of UserDiscoveryMixesItemsMultiRelationshipDataDocument from a dict
user_discovery_mixes_items_multi_relationship_data_document_from_dict = UserDiscoveryMixesItemsMultiRelationshipDataDocument.from_dict(user_discovery_mixes_items_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


