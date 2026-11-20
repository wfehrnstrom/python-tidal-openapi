# TracksSimilarTracksResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**TracksSimilarTracksResourceIdentifierMeta**](TracksSimilarTracksResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.tracks_similar_tracks_resource_identifier import TracksSimilarTracksResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TracksSimilarTracksResourceIdentifier from a JSON string
tracks_similar_tracks_resource_identifier_instance = TracksSimilarTracksResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(TracksSimilarTracksResourceIdentifier.to_json())

# convert the object into a dict
tracks_similar_tracks_resource_identifier_dict = tracks_similar_tracks_resource_identifier_instance.to_dict()
# create an instance of TracksSimilarTracksResourceIdentifier from a dict
tracks_similar_tracks_resource_identifier_from_dict = TracksSimilarTracksResourceIdentifier.from_dict(tracks_similar_tracks_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


