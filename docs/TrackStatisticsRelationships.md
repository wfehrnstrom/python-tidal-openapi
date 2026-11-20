# TrackStatisticsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**TrackStatisticsOwnersMultiRelationshipDataDocument**](TrackStatisticsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.track_statistics_relationships import TrackStatisticsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TrackStatisticsRelationships from a JSON string
track_statistics_relationships_instance = TrackStatisticsRelationships.from_json(json)
# print the JSON string representation of the object
print(TrackStatisticsRelationships.to_json())

# convert the object into a dict
track_statistics_relationships_dict = track_statistics_relationships_instance.to_dict()
# create an instance of TrackStatisticsRelationships from a dict
track_statistics_relationships_from_dict = TrackStatisticsRelationships.from_dict(track_statistics_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


