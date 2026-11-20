# TracksSuggestedTracksResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**TracksSuggestedTracksResourceIdentifierMeta**](TracksSuggestedTracksResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.tracks_suggested_tracks_resource_identifier import TracksSuggestedTracksResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TracksSuggestedTracksResourceIdentifier from a JSON string
tracks_suggested_tracks_resource_identifier_instance = TracksSuggestedTracksResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(TracksSuggestedTracksResourceIdentifier.to_json())

# convert the object into a dict
tracks_suggested_tracks_resource_identifier_dict = tracks_suggested_tracks_resource_identifier_instance.to_dict()
# create an instance of TracksSuggestedTracksResourceIdentifier from a dict
tracks_suggested_tracks_resource_identifier_from_dict = TracksSuggestedTracksResourceIdentifier.from_dict(tracks_suggested_tracks_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


