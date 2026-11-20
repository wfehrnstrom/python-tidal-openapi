# ArtistClaimsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_artists** | [**ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument**](ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**ArtistClaimsOwnersMultiRelationshipDataDocument**](ArtistClaimsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**recommended_artists** | [**ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument**](ArtistClaimsRecommendedArtistsMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.artist_claims_relationships import ArtistClaimsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsRelationships from a JSON string
artist_claims_relationships_instance = ArtistClaimsRelationships.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsRelationships.to_json())

# convert the object into a dict
artist_claims_relationships_dict = artist_claims_relationships_instance.to_dict()
# create an instance of ArtistClaimsRelationships from a dict
artist_claims_relationships_from_dict = ArtistClaimsRelationships.from_dict(artist_claims_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


