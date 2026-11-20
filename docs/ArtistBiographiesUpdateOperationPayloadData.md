# ArtistBiographiesUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistBiographiesUpdateOperationPayloadDataAttributes**](ArtistBiographiesUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.artist_biographies_update_operation_payload_data import ArtistBiographiesUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistBiographiesUpdateOperationPayloadData from a JSON string
artist_biographies_update_operation_payload_data_instance = ArtistBiographiesUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ArtistBiographiesUpdateOperationPayloadData.to_json())

# convert the object into a dict
artist_biographies_update_operation_payload_data_dict = artist_biographies_update_operation_payload_data_instance.to_dict()
# create an instance of ArtistBiographiesUpdateOperationPayloadData from a dict
artist_biographies_update_operation_payload_data_from_dict = ArtistBiographiesUpdateOperationPayloadData.from_dict(artist_biographies_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


