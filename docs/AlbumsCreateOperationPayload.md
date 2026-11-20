# AlbumsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlbumsCreateOperationPayloadData**](AlbumsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.albums_create_operation_payload import AlbumsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsCreateOperationPayload from a JSON string
albums_create_operation_payload_instance = AlbumsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(AlbumsCreateOperationPayload.to_json())

# convert the object into a dict
albums_create_operation_payload_dict = albums_create_operation_payload_instance.to_dict()
# create an instance of AlbumsCreateOperationPayload from a dict
albums_create_operation_payload_from_dict = AlbumsCreateOperationPayload.from_dict(albums_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


