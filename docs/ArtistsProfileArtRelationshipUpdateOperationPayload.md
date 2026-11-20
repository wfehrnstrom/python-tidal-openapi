# ArtistsProfileArtRelationshipUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsProfileArtRelationshipUpdateOperationPayloadData]**](ArtistsProfileArtRelationshipUpdateOperationPayloadData.md) |  | 
**meta** | [**AlbumsArtistsRelationshipUpdateOperationPayloadMeta**](AlbumsArtistsRelationshipUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.artists_profile_art_relationship_update_operation_payload import ArtistsProfileArtRelationshipUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsProfileArtRelationshipUpdateOperationPayload from a JSON string
artists_profile_art_relationship_update_operation_payload_instance = ArtistsProfileArtRelationshipUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistsProfileArtRelationshipUpdateOperationPayload.to_json())

# convert the object into a dict
artists_profile_art_relationship_update_operation_payload_dict = artists_profile_art_relationship_update_operation_payload_instance.to_dict()
# create an instance of ArtistsProfileArtRelationshipUpdateOperationPayload from a dict
artists_profile_art_relationship_update_operation_payload_from_dict = ArtistsProfileArtRelationshipUpdateOperationPayload.from_dict(artists_profile_art_relationship_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


