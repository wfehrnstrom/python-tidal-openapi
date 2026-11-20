# ArtistsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistsUpdateOperationPayloadData**](ArtistsUpdateOperationPayloadData.md) |  | 
**meta** | [**ArtistsUpdateOperationPayloadMeta**](ArtistsUpdateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.artists_update_operation_payload import ArtistsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsUpdateOperationPayload from a JSON string
artists_update_operation_payload_instance = ArtistsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistsUpdateOperationPayload.to_json())

# convert the object into a dict
artists_update_operation_payload_dict = artists_update_operation_payload_instance.to_dict()
# create an instance of ArtistsUpdateOperationPayload from a dict
artists_update_operation_payload_from_dict = ArtistsUpdateOperationPayload.from_dict(artists_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


