# ArtworksCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | **str** |  | 
**source_file** | [**ArtworksCreateOperationPayloadDataAttributesSourceFile**](ArtworksCreateOperationPayloadDataAttributesSourceFile.md) |  | 

## Example

```python
from tidal.models.artworks_create_operation_payload_data_attributes import ArtworksCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksCreateOperationPayloadDataAttributes from a JSON string
artworks_create_operation_payload_data_attributes_instance = ArtworksCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtworksCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
artworks_create_operation_payload_data_attributes_dict = artworks_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of ArtworksCreateOperationPayloadDataAttributes from a dict
artworks_create_operation_payload_data_attributes_from_dict = ArtworksCreateOperationPayloadDataAttributes.from_dict(artworks_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


