# PlaylistsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | User-selectable playlist visibility. | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from tidal.models.playlists_create_operation_payload_data_attributes import PlaylistsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCreateOperationPayloadDataAttributes from a JSON string
playlists_create_operation_payload_data_attributes_instance = PlaylistsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
playlists_create_operation_payload_data_attributes_dict = playlists_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of PlaylistsCreateOperationPayloadDataAttributes from a dict
playlists_create_operation_payload_data_attributes_from_dict = PlaylistsCreateOperationPayloadDataAttributes.from_dict(playlists_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


