# ArtworksCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtworksCreateOperationPayloadData**](ArtworksCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.artworks_create_operation_payload import ArtworksCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksCreateOperationPayload from a JSON string
artworks_create_operation_payload_instance = ArtworksCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtworksCreateOperationPayload.to_json())

# convert the object into a dict
artworks_create_operation_payload_dict = artworks_create_operation_payload_instance.to_dict()
# create an instance of ArtworksCreateOperationPayload from a dict
artworks_create_operation_payload_from_dict = ArtworksCreateOperationPayload.from_dict(artworks_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


