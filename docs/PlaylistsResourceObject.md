# PlaylistsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlaylistsAttributes**](PlaylistsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**PlaylistsRelationships**](PlaylistsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.playlists_resource_object import PlaylistsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsResourceObject from a JSON string
playlists_resource_object_instance = PlaylistsResourceObject.from_json(json)
# print the JSON string representation of the object
print(PlaylistsResourceObject.to_json())

# convert the object into a dict
playlists_resource_object_dict = playlists_resource_object_instance.to_dict()
# create an instance of PlaylistsResourceObject from a dict
playlists_resource_object_from_dict = PlaylistsResourceObject.from_dict(playlists_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


