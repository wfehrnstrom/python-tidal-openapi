# AlbumsCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artists** | [**AlbumsCreateOperationPayloadDataRelationshipsArtists**](AlbumsCreateOperationPayloadDataRelationshipsArtists.md) |  | 
**genres** | [**AlbumsCreateOperationPayloadDataRelationshipsGenres**](AlbumsCreateOperationPayloadDataRelationshipsGenres.md) |  | [optional] 

## Example

```python
from tidal.models.albums_create_operation_payload_data_relationships import AlbumsCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsCreateOperationPayloadDataRelationships from a JSON string
albums_create_operation_payload_data_relationships_instance = AlbumsCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(AlbumsCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
albums_create_operation_payload_data_relationships_dict = albums_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of AlbumsCreateOperationPayloadDataRelationships from a dict
albums_create_operation_payload_data_relationships_from_dict = AlbumsCreateOperationPayloadDataRelationships.from_dict(albums_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


