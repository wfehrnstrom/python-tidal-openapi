# VideosResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**VideosAttributes**](VideosAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**VideosRelationships**](VideosRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.videos_resource_object import VideosResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of VideosResourceObject from a JSON string
videos_resource_object_instance = VideosResourceObject.from_json(json)
# print the JSON string representation of the object
print(VideosResourceObject.to_json())

# convert the object into a dict
videos_resource_object_dict = videos_resource_object_instance.to_dict()
# create an instance of VideosResourceObject from a dict
videos_resource_object_from_dict = VideosResourceObject.from_dict(videos_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


