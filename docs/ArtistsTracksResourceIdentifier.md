# ArtistsTracksResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtistsTracksResourceIdentifierMeta**](ArtistsTracksResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artists_tracks_resource_identifier import ArtistsTracksResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsTracksResourceIdentifier from a JSON string
artists_tracks_resource_identifier_instance = ArtistsTracksResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtistsTracksResourceIdentifier.to_json())

# convert the object into a dict
artists_tracks_resource_identifier_dict = artists_tracks_resource_identifier_instance.to_dict()
# create an instance of ArtistsTracksResourceIdentifier from a dict
artists_tracks_resource_identifier_from_dict = ArtistsTracksResourceIdentifier.from_dict(artists_tracks_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


