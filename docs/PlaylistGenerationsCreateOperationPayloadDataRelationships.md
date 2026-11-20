# PlaylistGenerationsCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_generation** | [**PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGeneration**](PlaylistGenerationsCreateOperationPayloadDataRelationshipsBaseGeneration.md) |  | [optional] 
**playlist** | [**PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylist**](PlaylistGenerationsCreateOperationPayloadDataRelationshipsPlaylist.md) |  | 

## Example

```python
from tidal.models.playlist_generations_create_operation_payload_data_relationships import PlaylistGenerationsCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsCreateOperationPayloadDataRelationships from a JSON string
playlist_generations_create_operation_payload_data_relationships_instance = PlaylistGenerationsCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
playlist_generations_create_operation_payload_data_relationships_dict = playlist_generations_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of PlaylistGenerationsCreateOperationPayloadDataRelationships from a dict
playlist_generations_create_operation_payload_data_relationships_from_dict = PlaylistGenerationsCreateOperationPayloadDataRelationships.from_dict(playlist_generations_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


