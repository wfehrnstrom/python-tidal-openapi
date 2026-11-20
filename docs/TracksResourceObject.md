# TracksResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TracksAttributes**](TracksAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**TracksRelationships**](TracksRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.tracks_resource_object import TracksResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TracksResourceObject from a JSON string
tracks_resource_object_instance = TracksResourceObject.from_json(json)
# print the JSON string representation of the object
print(TracksResourceObject.to_json())

# convert the object into a dict
tracks_resource_object_dict = tracks_resource_object_instance.to_dict()
# create an instance of TracksResourceObject from a dict
tracks_resource_object_from_dict = TracksResourceObject.from_dict(tracks_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


