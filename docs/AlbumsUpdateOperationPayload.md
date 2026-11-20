# AlbumsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlbumsUpdateOperationPayloadData**](AlbumsUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.albums_update_operation_payload import AlbumsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsUpdateOperationPayload from a JSON string
albums_update_operation_payload_instance = AlbumsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(AlbumsUpdateOperationPayload.to_json())

# convert the object into a dict
albums_update_operation_payload_dict = albums_update_operation_payload_instance.to_dict()
# create an instance of AlbumsUpdateOperationPayload from a dict
albums_update_operation_payload_from_dict = AlbumsUpdateOperationPayload.from_dict(albums_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


