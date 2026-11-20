# ArtworksCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtworksCreateOperationPayloadDataAttributes**](ArtworksCreateOperationPayloadDataAttributes.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.artworks_create_operation_payload_data import ArtworksCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksCreateOperationPayloadData from a JSON string
artworks_create_operation_payload_data_instance = ArtworksCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ArtworksCreateOperationPayloadData.to_json())

# convert the object into a dict
artworks_create_operation_payload_data_dict = artworks_create_operation_payload_data_instance.to_dict()
# create an instance of ArtworksCreateOperationPayloadData from a dict
artworks_create_operation_payload_data_from_dict = ArtworksCreateOperationPayloadData.from_dict(artworks_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


