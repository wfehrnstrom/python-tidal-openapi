# TrackSourceFilesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TrackSourceFilesAttributes**](TrackSourceFilesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**TrackSourceFilesRelationships**](TrackSourceFilesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.track_source_files_resource_object import TrackSourceFilesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TrackSourceFilesResourceObject from a JSON string
track_source_files_resource_object_instance = TrackSourceFilesResourceObject.from_json(json)
# print the JSON string representation of the object
print(TrackSourceFilesResourceObject.to_json())

# convert the object into a dict
track_source_files_resource_object_dict = track_source_files_resource_object_instance.to_dict()
# create an instance of TrackSourceFilesResourceObject from a dict
track_source_files_resource_object_from_dict = TrackSourceFilesResourceObject.from_dict(track_source_files_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


