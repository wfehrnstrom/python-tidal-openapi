# ArtistBiographiesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistBiographiesResourceObject**](ArtistBiographiesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_biographies_single_resource_data_document import ArtistBiographiesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistBiographiesSingleResourceDataDocument from a JSON string
artist_biographies_single_resource_data_document_instance = ArtistBiographiesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistBiographiesSingleResourceDataDocument.to_json())

# convert the object into a dict
artist_biographies_single_resource_data_document_dict = artist_biographies_single_resource_data_document_instance.to_dict()
# create an instance of ArtistBiographiesSingleResourceDataDocument from a dict
artist_biographies_single_resource_data_document_from_dict = ArtistBiographiesSingleResourceDataDocument.from_dict(artist_biographies_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


