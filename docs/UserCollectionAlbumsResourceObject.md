# UserCollectionAlbumsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserCollectionAlbumsAttributes**](UserCollectionAlbumsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserCollectionAlbumsRelationships**](UserCollectionAlbumsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_albums_resource_object import UserCollectionAlbumsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionAlbumsResourceObject from a JSON string
user_collection_albums_resource_object_instance = UserCollectionAlbumsResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserCollectionAlbumsResourceObject.to_json())

# convert the object into a dict
user_collection_albums_resource_object_dict = user_collection_albums_resource_object_instance.to_dict()
# create an instance of UserCollectionAlbumsResourceObject from a dict
user_collection_albums_resource_object_from_dict = UserCollectionAlbumsResourceObject.from_dict(user_collection_albums_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


