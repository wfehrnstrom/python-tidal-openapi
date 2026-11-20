# TracksTrackStatisticsSingleRelationshipDataDocument

Target resource types: `trackStatistics`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_track_statistics_single_relationship_data_document import TracksTrackStatisticsSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksTrackStatisticsSingleRelationshipDataDocument from a JSON string
tracks_track_statistics_single_relationship_data_document_instance = TracksTrackStatisticsSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksTrackStatisticsSingleRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_track_statistics_single_relationship_data_document_dict = tracks_track_statistics_single_relationship_data_document_instance.to_dict()
# create an instance of TracksTrackStatisticsSingleRelationshipDataDocument from a dict
tracks_track_statistics_single_relationship_data_document_from_dict = TracksTrackStatisticsSingleRelationshipDataDocument.from_dict(tracks_track_statistics_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


