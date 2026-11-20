# AlbumsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**AlbumsUpdateOperationPayloadDataAttributes**](AlbumsUpdateOperationPayloadDataAttributes.md) |  | [optional] 
**id** | **str** |  | 
**relationships** | [**AlbumsUpdateOperationPayloadDataRelationships**](AlbumsUpdateOperationPayloadDataRelationships.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.albums_update_operation_payload_data import AlbumsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsUpdateOperationPayloadData from a JSON string
albums_update_operation_payload_data_instance = AlbumsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(AlbumsUpdateOperationPayloadData.to_json())

# convert the object into a dict
albums_update_operation_payload_data_dict = albums_update_operation_payload_data_instance.to_dict()
# create an instance of AlbumsUpdateOperationPayloadData from a dict
albums_update_operation_payload_data_from_dict = AlbumsUpdateOperationPayloadData.from_dict(albums_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


