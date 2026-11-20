# ArtistsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistsResourceObject**](ArtistsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_single_resource_data_document import ArtistsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsSingleResourceDataDocument from a JSON string
artists_single_resource_data_document_instance = ArtistsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsSingleResourceDataDocument.to_json())

# convert the object into a dict
artists_single_resource_data_document_dict = artists_single_resource_data_document_instance.to_dict()
# create an instance of ArtistsSingleResourceDataDocument from a dict
artists_single_resource_data_document_from_dict = ArtistsSingleResourceDataDocument.from_dict(artists_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


