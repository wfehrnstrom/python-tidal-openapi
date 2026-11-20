# TrackFilesReadById403ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[TrackFilesReadById403ResponseBodyErrorsInner]**](TrackFilesReadById403ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.track_files_read_by_id403_response_body import TrackFilesReadById403ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TrackFilesReadById403ResponseBody from a JSON string
track_files_read_by_id403_response_body_instance = TrackFilesReadById403ResponseBody.from_json(json)
# print the JSON string representation of the object
print(TrackFilesReadById403ResponseBody.to_json())

# convert the object into a dict
track_files_read_by_id403_response_body_dict = track_files_read_by_id403_response_body_instance.to_dict()
# create an instance of TrackFilesReadById403ResponseBody from a dict
track_files_read_by_id403_response_body_from_dict = TrackFilesReadById403ResponseBody.from_dict(track_files_read_by_id403_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


