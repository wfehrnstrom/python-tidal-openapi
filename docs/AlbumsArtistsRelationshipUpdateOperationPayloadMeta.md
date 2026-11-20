# AlbumsArtistsRelationshipUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Relationship mutation mode. INCREMENTAL updates selected existing entries without adding or removing memberships; REPLACE_ALL replaces the complete membership and its order where applicable. Omission defaults to REPLACE_ALL. | [optional] [default to 'REPLACE_ALL']

## Example

```python
from tidal.models.albums_artists_relationship_update_operation_payload_meta import AlbumsArtistsRelationshipUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsArtistsRelationshipUpdateOperationPayloadMeta from a JSON string
albums_artists_relationship_update_operation_payload_meta_instance = AlbumsArtistsRelationshipUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(AlbumsArtistsRelationshipUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
albums_artists_relationship_update_operation_payload_meta_dict = albums_artists_relationship_update_operation_payload_meta_instance.to_dict()
# create an instance of AlbumsArtistsRelationshipUpdateOperationPayloadMeta from a dict
albums_artists_relationship_update_operation_payload_meta_from_dict = AlbumsArtistsRelationshipUpdateOperationPayloadMeta.from_dict(albums_artists_relationship_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


