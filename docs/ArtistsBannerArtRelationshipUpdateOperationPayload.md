# ArtistsBannerArtRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsBannerArtRelationshipUpdateOperationPayloadData]**](ArtistsBannerArtRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.artists_banner_art_relationship_update_operation_payload import ArtistsBannerArtRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsBannerArtRelationshipUpdateOperationPayload from a JSON string
artists_banner_art_relationship_update_operation_payload_instance = ArtistsBannerArtRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistsBannerArtRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
artists_banner_art_relationship_update_operation_payload_dict = artists_banner_art_relationship_update_operation_payload_instance.to_dict()
# create an instance of ArtistsBannerArtRelationshipUpdateOperationPayload from a dict
artists_banner_art_relationship_update_operation_payload_from_dict = ArtistsBannerArtRelationshipUpdateOperationPayload.from_dict(artists_banner_art_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


