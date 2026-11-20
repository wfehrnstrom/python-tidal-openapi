# TracksCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**TracksCreateOperationPayloadDataRelationshipsAlbums**](TracksCreateOperationPayloadDataRelationshipsAlbums.md) |  | 
**artists** | [**TracksCreateOperationPayloadDataRelationshipsArtists**](TracksCreateOperationPayloadDataRelationshipsArtists.md) |  | 
**genres** | [**TracksCreateOperationPayloadDataRelationshipsGenres**](TracksCreateOperationPayloadDataRelationshipsGenres.md) |  | [optional] 

## Example

```python
from tidal.models.tracks_create_operation_payload_data_relationships import TracksCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TracksCreateOperationPayloadDataRelationships from a JSON string
tracks_create_operation_payload_data_relationships_instance = TracksCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(TracksCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
tracks_create_operation_payload_data_relationships_dict = tracks_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of TracksCreateOperationPayloadDataRelationships from a dict
tracks_create_operation_payload_data_relationships_from_dict = TracksCreateOperationPayloadDataRelationships.from_dict(tracks_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


