# TrackManifestsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TrackManifestsAttributes**](TrackManifestsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.track_manifests_resource_object import TrackManifestsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TrackManifestsResourceObject from a JSON string
track_manifests_resource_object_instance = TrackManifestsResourceObject.from_json(json)
# print the JSON string representation of the object
print(TrackManifestsResourceObject.to_json())

# convert the object into a dict
track_manifests_resource_object_dict = track_manifests_resource_object_instance.to_dict()
# create an instance of TrackManifestsResourceObject from a dict
track_manifests_resource_object_from_dict = TrackManifestsResourceObject.from_dict(track_manifests_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


