# ArtistsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistsUpdateOperationPayloadDataAttributes**](ArtistsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.artists_update_operation_payload_data import ArtistsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsUpdateOperationPayloadData from a JSON string
artists_update_operation_payload_data_instance = ArtistsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ArtistsUpdateOperationPayloadData.to_json())

# convert the object into a dict
artists_update_operation_payload_data_dict = artists_update_operation_payload_data_instance.to_dict()
# create an instance of ArtistsUpdateOperationPayloadData from a dict
artists_update_operation_payload_data_from_dict = ArtistsUpdateOperationPayloadData.from_dict(artists_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


