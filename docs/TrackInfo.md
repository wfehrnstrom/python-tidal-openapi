# TrackInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broken** | **bool** |  | [optional] 
**broken_code** | **int** |  | [optional] 
**track_id** | **str** |  | 

## Example

```python
from tidal.models.track_info import TrackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrackInfo from a JSON string
track_info_instance = TrackInfo.from_json(json)
# print the JSON string representation of the object
print(TrackInfo.to_json())

# convert the object into a dict
track_info_dict = track_info_instance.to_dict()
# create an instance of TrackInfo from a dict
track_info_from_dict = TrackInfo.from_dict(track_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


