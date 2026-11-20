# ArtistsUpdateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 

## Example

```python
from tidal.models.artists_update_operation_payload_meta import ArtistsUpdateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsUpdateOperationPayloadMeta from a JSON string
artists_update_operation_payload_meta_instance = ArtistsUpdateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistsUpdateOperationPayloadMeta.to_json())

# convert the object into a dict
artists_update_operation_payload_meta_dict = artists_update_operation_payload_meta_instance.to_dict()
# create an instance of ArtistsUpdateOperationPayloadMeta from a dict
artists_update_operation_payload_meta_from_dict = ArtistsUpdateOperationPayloadMeta.from_dict(artists_update_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


