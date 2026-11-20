# ArtistsTracksResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.artists_tracks_resource_identifier_meta import ArtistsTracksResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsTracksResourceIdentifierMeta from a JSON string
artists_tracks_resource_identifier_meta_instance = ArtistsTracksResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistsTracksResourceIdentifierMeta.to_json())

# convert the object into a dict
artists_tracks_resource_identifier_meta_dict = artists_tracks_resource_identifier_meta_instance.to_dict()
# create an instance of ArtistsTracksResourceIdentifierMeta from a dict
artists_tracks_resource_identifier_meta_from_dict = ArtistsTracksResourceIdentifierMeta.from_dict(artists_tracks_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


