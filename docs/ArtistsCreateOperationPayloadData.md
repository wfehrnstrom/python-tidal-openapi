# ArtistsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistsCreateOperationPayloadDataAttributes**](ArtistsCreateOperationPayloadDataAttributes.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.artists_create_operation_payload_data import ArtistsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsCreateOperationPayloadData from a JSON string
artists_create_operation_payload_data_instance = ArtistsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ArtistsCreateOperationPayloadData.to_json())

# convert the object into a dict
artists_create_operation_payload_data_dict = artists_create_operation_payload_data_instance.to_dict()
# create an instance of ArtistsCreateOperationPayloadData from a dict
artists_create_operation_payload_data_from_dict = ArtistsCreateOperationPayloadData.from_dict(artists_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


