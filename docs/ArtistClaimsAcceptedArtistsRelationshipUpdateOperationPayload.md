# ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayloadData]**](ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.artist_claims_accepted_artists_relationship_update_operation_payload import ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload from a JSON string
artist_claims_accepted_artists_relationship_update_operation_payload_instance = ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
artist_claims_accepted_artists_relationship_update_operation_payload_dict = artist_claims_accepted_artists_relationship_update_operation_payload_instance.to_dict()
# create an instance of ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload from a dict
artist_claims_accepted_artists_relationship_update_operation_payload_from_dict = ArtistClaimsAcceptedArtistsRelationshipUpdateOperationPayload.from_dict(artist_claims_accepted_artists_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


