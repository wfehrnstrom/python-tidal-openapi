# AlbumsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**AlbumsCreateOperationPayloadDataAttributes**](AlbumsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**AlbumsCreateOperationPayloadDataRelationships**](AlbumsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.albums_create_operation_payload_data import AlbumsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsCreateOperationPayloadData from a JSON string
albums_create_operation_payload_data_instance = AlbumsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(AlbumsCreateOperationPayloadData.to_json())

# convert the object into a dict
albums_create_operation_payload_data_dict = albums_create_operation_payload_data_instance.to_dict()
# create an instance of AlbumsCreateOperationPayloadData from a dict
albums_create_operation_payload_data_from_dict = AlbumsCreateOperationPayloadData.from_dict(albums_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


