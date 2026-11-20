# UserCollectionVideosItemsAddResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**UserCollectionVideosItemsAddResourceIdentifierMeta**](UserCollectionVideosItemsAddResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_collection_videos_items_add_resource_identifier import UserCollectionVideosItemsAddResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionVideosItemsAddResourceIdentifier from a JSON string
user_collection_videos_items_add_resource_identifier_instance = UserCollectionVideosItemsAddResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(UserCollectionVideosItemsAddResourceIdentifier.to_json())

# convert the object into a dict
user_collection_videos_items_add_resource_identifier_dict = user_collection_videos_items_add_resource_identifier_instance.to_dict()
# create an instance of UserCollectionVideosItemsAddResourceIdentifier from a dict
user_collection_videos_items_add_resource_identifier_from_dict = UserCollectionVideosItemsAddResourceIdentifier.from_dict(user_collection_videos_items_add_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


