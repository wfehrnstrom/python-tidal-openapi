# PlaylistGenerationsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistGenerationsCreateOperationPayloadData**](PlaylistGenerationsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.playlist_generations_create_operation_payload import PlaylistGenerationsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsCreateOperationPayload from a JSON string
playlist_generations_create_operation_payload_instance = PlaylistGenerationsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsCreateOperationPayload.to_json())

# convert the object into a dict
playlist_generations_create_operation_payload_dict = playlist_generations_create_operation_payload_instance.to_dict()
# create an instance of PlaylistGenerationsCreateOperationPayload from a dict
playlist_generations_create_operation_payload_from_dict = PlaylistGenerationsCreateOperationPayload.from_dict(playlist_generations_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


