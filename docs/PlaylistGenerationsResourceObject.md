# PlaylistGenerationsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlaylistGenerationsAttributes**](PlaylistGenerationsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**PlaylistGenerationsRelationships**](PlaylistGenerationsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.playlist_generations_resource_object import PlaylistGenerationsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsResourceObject from a JSON string
playlist_generations_resource_object_instance = PlaylistGenerationsResourceObject.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsResourceObject.to_json())

# convert the object into a dict
playlist_generations_resource_object_dict = playlist_generations_resource_object_instance.to_dict()
# create an instance of PlaylistGenerationsResourceObject from a dict
playlist_generations_resource_object_from_dict = PlaylistGenerationsResourceObject.from_dict(playlist_generations_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


