# TracksMetadataStatusResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TracksMetadataStatusAttributes**](TracksMetadataStatusAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.tracks_metadata_status_resource_object import TracksMetadataStatusResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TracksMetadataStatusResourceObject from a JSON string
tracks_metadata_status_resource_object_instance = TracksMetadataStatusResourceObject.from_json(json)
# print the JSON string representation of the object
print(TracksMetadataStatusResourceObject.to_json())

# convert the object into a dict
tracks_metadata_status_resource_object_dict = tracks_metadata_status_resource_object_instance.to_dict()
# create an instance of TracksMetadataStatusResourceObject from a dict
tracks_metadata_status_resource_object_from_dict = TracksMetadataStatusResourceObject.from_dict(tracks_metadata_status_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


