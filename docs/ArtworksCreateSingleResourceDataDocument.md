# ArtworksCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtworksResourceObject**](ArtworksResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artworks_create_single_resource_data_document import ArtworksCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksCreateSingleResourceDataDocument from a JSON string
artworks_create_single_resource_data_document_instance = ArtworksCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtworksCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
artworks_create_single_resource_data_document_dict = artworks_create_single_resource_data_document_instance.to_dict()
# create an instance of ArtworksCreateSingleResourceDataDocument from a dict
artworks_create_single_resource_data_document_from_dict = ArtworksCreateSingleResourceDataDocument.from_dict(artworks_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


