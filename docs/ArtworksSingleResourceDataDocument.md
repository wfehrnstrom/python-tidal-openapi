# ArtworksSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtworksResourceObject**](ArtworksResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artworks_single_resource_data_document import ArtworksSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksSingleResourceDataDocument from a JSON string
artworks_single_resource_data_document_instance = ArtworksSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtworksSingleResourceDataDocument.to_json())

# convert the object into a dict
artworks_single_resource_data_document_dict = artworks_single_resource_data_document_instance.to_dict()
# create an instance of ArtworksSingleResourceDataDocument from a dict
artworks_single_resource_data_document_from_dict = ArtworksSingleResourceDataDocument.from_dict(artworks_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


