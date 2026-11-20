# TrackStatisticsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_playbacks** | **int** | Total playbacks | 
**unique_listeners** | **int** | Unique listeners | 

## Example

```python
from tidal.models.track_statistics_attributes import TrackStatisticsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TrackStatisticsAttributes from a JSON string
track_statistics_attributes_instance = TrackStatisticsAttributes.from_json(json)
# print the JSON string representation of the object
print(TrackStatisticsAttributes.to_json())

# convert the object into a dict
track_statistics_attributes_dict = track_statistics_attributes_instance.to_dict()
# create an instance of TrackStatisticsAttributes from a dict
track_statistics_attributes_from_dict = TrackStatisticsAttributes.from_dict(track_statistics_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


