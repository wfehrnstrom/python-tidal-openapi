# ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_claims_accepted_artists_multi_relationship_data_document import ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument from a JSON string
artist_claims_accepted_artists_multi_relationship_data_document_instance = ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artist_claims_accepted_artists_multi_relationship_data_document_dict = artist_claims_accepted_artists_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument from a dict
artist_claims_accepted_artists_multi_relationship_data_document_from_dict = ArtistClaimsAcceptedArtistsMultiRelationshipDataDocument.from_dict(artist_claims_accepted_artists_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


