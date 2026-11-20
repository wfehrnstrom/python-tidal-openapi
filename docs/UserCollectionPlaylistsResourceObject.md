# UserCollectionPlaylistsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserCollectionPlaylistsAttributes**](UserCollectionPlaylistsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserCollectionPlaylistsRelationships**](UserCollectionPlaylistsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_playlists_resource_object import UserCollectionPlaylistsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionPlaylistsResourceObject from a JSON string
user_collection_playlists_resource_object_instance = UserCollectionPlaylistsResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserCollectionPlaylistsResourceObject.to_json())

# convert the object into a dict
user_collection_playlists_resource_object_dict = user_collection_playlists_resource_object_instance.to_dict()
# create an instance of UserCollectionPlaylistsResourceObject from a dict
user_collection_playlists_resource_object_from_dict = UserCollectionPlaylistsResourceObject.from_dict(user_collection_playlists_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


