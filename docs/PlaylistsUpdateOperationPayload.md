# PlaylistsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaylistsUpdateOperationPayloadData**](PlaylistsUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.playlists_update_operation_payload import PlaylistsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsUpdateOperationPayload from a JSON string
playlists_update_operation_payload_instance = PlaylistsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(PlaylistsUpdateOperationPayload.to_json())

# convert the object into a dict
playlists_update_operation_payload_dict = playlists_update_operation_payload_instance.to_dict()
# create an instance of PlaylistsUpdateOperationPayload from a dict
playlists_update_operation_payload_from_dict = PlaylistsUpdateOperationPayload.from_dict(playlists_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


