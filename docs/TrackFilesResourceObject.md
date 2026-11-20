# TrackFilesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TrackFilesAttributes**](TrackFilesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.track_files_resource_object import TrackFilesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TrackFilesResourceObject from a JSON string
track_files_resource_object_instance = TrackFilesResourceObject.from_json(json)
# print the JSON string representation of the object
print(TrackFilesResourceObject.to_json())

# convert the object into a dict
track_files_resource_object_dict = track_files_resource_object_instance.to_dict()
# create an instance of TrackFilesResourceObject from a dict
track_files_resource_object_from_dict = TrackFilesResourceObject.from_dict(track_files_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


