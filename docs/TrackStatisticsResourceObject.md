# TrackStatisticsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**TrackStatisticsAttributes**](TrackStatisticsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**TrackStatisticsRelationships**](TrackStatisticsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.track_statistics_resource_object import TrackStatisticsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TrackStatisticsResourceObject from a JSON string
track_statistics_resource_object_instance = TrackStatisticsResourceObject.from_json(json)
# print the JSON string representation of the object
print(TrackStatisticsResourceObject.to_json())

# convert the object into a dict
track_statistics_resource_object_dict = track_statistics_resource_object_instance.to_dict()
# create an instance of TrackStatisticsResourceObject from a dict
track_statistics_resource_object_from_dict = TrackStatisticsResourceObject.from_dict(track_statistics_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


