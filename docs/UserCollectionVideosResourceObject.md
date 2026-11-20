# UserCollectionVideosResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserCollectionVideosAttributes**](UserCollectionVideosAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserCollectionVideosRelationships**](UserCollectionVideosRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_collection_videos_resource_object import UserCollectionVideosResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionVideosResourceObject from a JSON string
user_collection_videos_resource_object_instance = UserCollectionVideosResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserCollectionVideosResourceObject.to_json())

# convert the object into a dict
user_collection_videos_resource_object_dict = user_collection_videos_resource_object_instance.to_dict()
# create an instance of UserCollectionVideosResourceObject from a dict
user_collection_videos_resource_object_from_dict = UserCollectionVideosResourceObject.from_dict(user_collection_videos_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


