# UserCollectionSaveForLatersRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserCollectionSaveForLatersItemsMultiRelationshipDataDocument**](UserCollectionSaveForLatersItemsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument**](UserCollectionSaveForLatersOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_collection_save_for_laters_relationships import UserCollectionSaveForLatersRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionSaveForLatersRelationships from a JSON string
user_collection_save_for_laters_relationships_instance = UserCollectionSaveForLatersRelationships.from_json(json)
# print the JSON string representation of the object
print(UserCollectionSaveForLatersRelationships.to_json())

# convert the object into a dict
user_collection_save_for_laters_relationships_dict = user_collection_save_for_laters_relationships_instance.to_dict()
# create an instance of UserCollectionSaveForLatersRelationships from a dict
user_collection_save_for_laters_relationships_from_dict = UserCollectionSaveForLatersRelationships.from_dict(user_collection_save_for_laters_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


