# ArtistBiographiesUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistBiographiesUpdateOperationPayloadData**](ArtistBiographiesUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.artist_biographies_update_operation_payload import ArtistBiographiesUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistBiographiesUpdateOperationPayload from a JSON string
artist_biographies_update_operation_payload_instance = ArtistBiographiesUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistBiographiesUpdateOperationPayload.to_json())

# convert the object into a dict
artist_biographies_update_operation_payload_dict = artist_biographies_update_operation_payload_instance.to_dict()
# create an instance of ArtistBiographiesUpdateOperationPayload from a dict
artist_biographies_update_operation_payload_from_dict = ArtistBiographiesUpdateOperationPayload.from_dict(artist_biographies_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


