# PlaylistGenerationsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preference_version** | **int** | Current track-preference version | [optional] 
**prompt** | **str** |  | 

## Example

```python
from tidal.models.playlist_generations_create_operation_payload_data_attributes import PlaylistGenerationsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistGenerationsCreateOperationPayloadDataAttributes from a JSON string
playlist_generations_create_operation_payload_data_attributes_instance = PlaylistGenerationsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(PlaylistGenerationsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
playlist_generations_create_operation_payload_data_attributes_dict = playlist_generations_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of PlaylistGenerationsCreateOperationPayloadDataAttributes from a dict
playlist_generations_create_operation_payload_data_attributes_from_dict = PlaylistGenerationsCreateOperationPayloadDataAttributes.from_dict(playlist_generations_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


