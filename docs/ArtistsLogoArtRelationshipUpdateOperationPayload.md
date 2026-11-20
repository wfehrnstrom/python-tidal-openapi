# ArtistsLogoArtRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsLogoArtRelationshipUpdateOperationPayloadData]**](ArtistsLogoArtRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.artists_logo_art_relationship_update_operation_payload import ArtistsLogoArtRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsLogoArtRelationshipUpdateOperationPayload from a JSON string
artists_logo_art_relationship_update_operation_payload_instance = ArtistsLogoArtRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistsLogoArtRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
artists_logo_art_relationship_update_operation_payload_dict = artists_logo_art_relationship_update_operation_payload_instance.to_dict()
# create an instance of ArtistsLogoArtRelationshipUpdateOperationPayload from a dict
artists_logo_art_relationship_update_operation_payload_from_dict = ArtistsLogoArtRelationshipUpdateOperationPayload.from_dict(artists_logo_art_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


