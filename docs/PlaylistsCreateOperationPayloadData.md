# PlaylistsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlaylistsCreateOperationPayloadDataAttributes**](PlaylistsCreateOperationPayloadDataAttributes.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.playlists_create_operation_payload_data import PlaylistsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCreateOperationPayloadData from a JSON string
playlists_create_operation_payload_data_instance = PlaylistsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCreateOperationPayloadData.to_json())

# convert the object into a dict
playlists_create_operation_payload_data_dict = playlists_create_operation_payload_data_instance.to_dict()
# create an instance of PlaylistsCreateOperationPayloadData from a dict
playlists_create_operation_payload_data_from_dict = PlaylistsCreateOperationPayloadData.from_dict(playlists_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


