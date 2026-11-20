# TracksUpdateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genres** | [**TracksUpdateOperationPayloadDataRelationshipsGenres**](TracksUpdateOperationPayloadDataRelationshipsGenres.md) |  | [optional] 

## Example

```python
from tidal.models.tracks_update_operation_payload_data_relationships import TracksUpdateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TracksUpdateOperationPayloadDataRelationships from a JSON string
tracks_update_operation_payload_data_relationships_instance = TracksUpdateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(TracksUpdateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
tracks_update_operation_payload_data_relationships_dict = tracks_update_operation_payload_data_relationships_instance.to_dict()
# create an instance of TracksUpdateOperationPayloadDataRelationships from a dict
tracks_update_operation_payload_data_relationships_from_dict = TracksUpdateOperationPayloadDataRelationships.from_dict(tracks_update_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


