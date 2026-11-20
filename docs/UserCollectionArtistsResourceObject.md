# UserCollectionArtistsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserCollectionArtistsAttributes**](UserCollectionArtistsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserCollectionArtistsRelationships**](UserCollectionArtistsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_artists_resource_object import UserCollectionArtistsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionArtistsResourceObject from a JSON string
user_collection_artists_resource_object_instance = UserCollectionArtistsResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserCollectionArtistsResourceObject.to_json())

# convert the object into a dict
user_collection_artists_resource_object_dict = user_collection_artists_resource_object_instance.to_dict()
# create an instance of UserCollectionArtistsResourceObject from a dict
user_collection_artists_resource_object_from_dict = UserCollectionArtistsResourceObject.from_dict(user_collection_artists_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


