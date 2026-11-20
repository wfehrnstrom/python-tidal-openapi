# PlaylistsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlaylistsUpdateOperationPayloadDataAttributes**](PlaylistsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlists_update_operation_payload_data import PlaylistsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsUpdateOperationPayloadData from a JSON string
playlists_update_operation_payload_data_instance = PlaylistsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistsUpdateOperationPayloadData.to_json())

# convert the object into a dict
playlists_update_operation_payload_data_dict = playlists_update_operation_payload_data_instance.to_dict()
# create an instance of PlaylistsUpdateOperationPayloadData from a dict
playlists_update_operation_payload_data_from_dict = PlaylistsUpdateOperationPayloadData.from_dict(playlists_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


