# AlbumsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | Access type | [optional] 
**album_type** | **str** |  | [optional] 
**barcode_id** | **str** | A barcode the rights holder already owns: a GTIN-12 or GTIN-13 (UPC-A or EAN-13) with a valid GS1 check digit. A barcode set here can be replaced until the album is first sold, and null resets it to the default value. An empty string is also accepted as a reset for now, for compatibility. After the first sale both are rejected. The barcode TIDAL assigns at the album&#39;s first sale is permanent. Omit the field to leave the barcode unchanged. Only the album&#39;s owners can set it. | [optional] 
**copyright** | [**Copyright**](Copyright.md) |  | [optional] 
**explicit** | **bool** | Explicit content | [optional] 
**explicit_lyrics** | **bool** | Explicit content. Deprecated: use &#39;explicit&#39; instead. This field will be removed in a future version. | [optional] 
**published** | **bool** | Whether the album is published to everyone. | [optional] 
**release_date** | **date** |  | [optional] 
**title** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from tidal.models.albums_update_operation_payload_data_attributes import AlbumsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsUpdateOperationPayloadDataAttributes from a JSON string
albums_update_operation_payload_data_attributes_instance = AlbumsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(AlbumsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
albums_update_operation_payload_data_attributes_dict = albums_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of AlbumsUpdateOperationPayloadDataAttributes from a dict
albums_update_operation_payload_data_attributes_from_dict = AlbumsUpdateOperationPayloadDataAttributes.from_dict(albums_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


