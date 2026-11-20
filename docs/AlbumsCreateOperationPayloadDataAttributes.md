# AlbumsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_type** | **str** |  | [optional] 
**copyright** | [**Copyright**](Copyright.md) |  | [optional] 
**explicit** | **bool** | Explicit content | [optional] 
**explicit_lyrics** | **bool** | Explicit content. Deprecated: use &#39;explicit&#39; instead. This field will be removed in a future version. | [optional] 
**release_date** | **date** |  | [optional] 
**title** | **str** |  | 
**version** | **str** |  | [optional] 

## Example

```python
from tidal.models.albums_create_operation_payload_data_attributes import AlbumsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsCreateOperationPayloadDataAttributes from a JSON string
albums_create_operation_payload_data_attributes_instance = AlbumsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(AlbumsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
albums_create_operation_payload_data_attributes_dict = albums_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of AlbumsCreateOperationPayloadDataAttributes from a dict
albums_create_operation_payload_data_attributes_from_dict = AlbumsCreateOperationPayloadDataAttributes.from_dict(albums_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


