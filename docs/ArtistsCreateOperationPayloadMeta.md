# ArtistsCreateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 

## Example

```python
from tidal.models.artists_create_operation_payload_meta import ArtistsCreateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsCreateOperationPayloadMeta from a JSON string
artists_create_operation_payload_meta_instance = ArtistsCreateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(ArtistsCreateOperationPayloadMeta.to_json())

# convert the object into a dict
artists_create_operation_payload_meta_dict = artists_create_operation_payload_meta_instance.to_dict()
# create an instance of ArtistsCreateOperationPayloadMeta from a dict
artists_create_operation_payload_meta_from_dict = ArtistsCreateOperationPayloadMeta.from_dict(artists_create_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


