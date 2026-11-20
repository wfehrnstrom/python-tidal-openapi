# ArtistsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistsCreateOperationPayloadData**](ArtistsCreateOperationPayloadData.md) |  | 
**meta** | [**ArtistsCreateOperationPayloadMeta**](ArtistsCreateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.artists_create_operation_payload import ArtistsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsCreateOperationPayload from a JSON string
artists_create_operation_payload_instance = ArtistsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistsCreateOperationPayload.to_json())

# convert the object into a dict
artists_create_operation_payload_dict = artists_create_operation_payload_instance.to_dict()
# create an instance of ArtistsCreateOperationPayload from a dict
artists_create_operation_payload_from_dict = ArtistsCreateOperationPayload.from_dict(artists_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


