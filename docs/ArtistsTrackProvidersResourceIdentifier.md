# ArtistsTrackProvidersResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtistsTrackProvidersResourceIdentifierMeta**](ArtistsTrackProvidersResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artists_track_providers_resource_identifier import ArtistsTrackProvidersResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsTrackProvidersResourceIdentifier from a JSON string
artists_track_providers_resource_identifier_instance = ArtistsTrackProvidersResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtistsTrackProvidersResourceIdentifier.to_json())

# convert the object into a dict
artists_track_providers_resource_identifier_dict = artists_track_providers_resource_identifier_instance.to_dict()
# create an instance of ArtistsTrackProvidersResourceIdentifier from a dict
artists_track_providers_resource_identifier_from_dict = ArtistsTrackProvidersResourceIdentifier.from_dict(artists_track_providers_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


