# ArtistsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**ArtistsAlbumsMultiRelationshipDataDocument**](ArtistsAlbumsMultiRelationshipDataDocument.md) |  | [optional] 
**banner_art** | [**ArtistsBannerArtMultiRelationshipDataDocument**](ArtistsBannerArtMultiRelationshipDataDocument.md) |  | [optional] 
**biography** | [**ArtistsBiographySingleRelationshipDataDocument**](ArtistsBiographySingleRelationshipDataDocument.md) |  | [optional] 
**claim_status** | [**ArtistsClaimStatusSingleRelationshipDataDocument**](ArtistsClaimStatusSingleRelationshipDataDocument.md) |  | [optional] 
**followers** | [**ArtistsFollowersMultiRelationshipDataDocument**](ArtistsFollowersMultiRelationshipDataDocument.md) |  | [optional] 
**following** | [**ArtistsFollowingMultiRelationshipDataDocument**](ArtistsFollowingMultiRelationshipDataDocument.md) |  | [optional] 
**logo_art** | [**ArtistsLogoArtMultiRelationshipDataDocument**](ArtistsLogoArtMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**ArtistsOwnersMultiRelationshipDataDocument**](ArtistsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**profile_art** | [**ArtistsProfileArtMultiRelationshipDataDocument**](ArtistsProfileArtMultiRelationshipDataDocument.md) |  | [optional] 
**radio** | [**ArtistsRadioMultiRelationshipDataDocument**](ArtistsRadioMultiRelationshipDataDocument.md) |  | [optional] 
**roles** | [**ArtistsRolesMultiRelationshipDataDocument**](ArtistsRolesMultiRelationshipDataDocument.md) |  | [optional] 
**similar_artists** | [**ArtistsSimilarArtistsMultiRelationshipDataDocument**](ArtistsSimilarArtistsMultiRelationshipDataDocument.md) |  | [optional] 
**track_providers** | [**ArtistsTrackProvidersMultiRelationshipDataDocument**](ArtistsTrackProvidersMultiRelationshipDataDocument.md) |  | [optional] 
**tracks** | [**ArtistsTracksMultiRelationshipDataDocument**](ArtistsTracksMultiRelationshipDataDocument.md) |  | [optional] 
**videos** | [**ArtistsVideosMultiRelationshipDataDocument**](ArtistsVideosMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.artists_relationships import ArtistsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsRelationships from a JSON string
artists_relationships_instance = ArtistsRelationships.from_json(json)
# print the JSON string representation of the object
print(ArtistsRelationships.to_json())

# convert the object into a dict
artists_relationships_dict = artists_relationships_instance.to_dict()
# create an instance of ArtistsRelationships from a dict
artists_relationships_from_dict = ArtistsRelationships.from_dict(artists_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


