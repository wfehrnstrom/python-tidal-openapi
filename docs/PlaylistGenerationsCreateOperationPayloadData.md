# PlaylistGenerationsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlaylistGenerationsCreateOperationPayloadDataAttributes**](PlaylistGenerationsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**PlaylistGenerationsCreateOperationPayloadDataRelationships**](PlaylistGenerationsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlist_generations_create_operation_payload_data import PlaylistGenerationsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsCreateOperationPayloadData from a JSON string
playlist_generations_create_operation_payload_data_instance = PlaylistGenerationsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsCreateOperationPayloadData.to_json())

# convert the object into a dict
playlist_generations_create_operation_payload_data_dict = playlist_generations_create_operation_payload_data_instance.to_dict()
# create an instance of PlaylistGenerationsCreateOperationPayloadData from a dict
playlist_generations_create_operation_payload_data_from_dict = PlaylistGenerationsCreateOperationPayloadData.from_dict(playlist_generations_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


