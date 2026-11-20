# TrackManifestsReadById404ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[TrackFilesReadById404ResponseBodyErrorsInner]**](TrackFilesReadById404ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.track_manifests_read_by_id404_response_body import TrackManifestsReadById404ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TrackManifestsReadById404ResponseBody from a JSON string
track_manifests_read_by_id404_response_body_instance = TrackManifestsReadById404ResponseBody.from_json(json)
# print the JSON string representation of the object
print(TrackManifestsReadById404ResponseBody.to_json())

# convert the object into a dict
track_manifests_read_by_id404_response_body_dict = track_manifests_read_by_id404_response_body_instance.to_dict()
# create an instance of TrackManifestsReadById404ResponseBody from a dict
track_manifests_read_by_id404_response_body_from_dict = TrackManifestsReadById404ResponseBody.from_dict(track_manifests_read_by_id404_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


