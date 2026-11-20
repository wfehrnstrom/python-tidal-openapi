# PlaylistsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistsCreateOperationPayloadData**](PlaylistsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.playlists_create_operation_payload import PlaylistsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCreateOperationPayload from a JSON string
playlists_create_operation_payload_instance = PlaylistsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCreateOperationPayload.to_json())

# convert the object into a dict
playlists_create_operation_payload_dict = playlists_create_operation_payload_instance.to_dict()
# create an instance of PlaylistsCreateOperationPayload from a dict
playlists_create_operation_payload_from_dict = PlaylistsCreateOperationPayload.from_dict(playlists_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


