# ArtistClaimsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistClaimsResourceObject]**](ArtistClaimsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_claims_multi_resource_data_document import ArtistClaimsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsMultiResourceDataDocument from a JSON string
artist_claims_multi_resource_data_document_instance = ArtistClaimsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsMultiResourceDataDocument.to_json())

# convert the object into a dict
artist_claims_multi_resource_data_document_dict = artist_claims_multi_resource_data_document_instance.to_dict()
# create an instance of ArtistClaimsMultiResourceDataDocument from a dict
artist_claims_multi_resource_data_document_from_dict = ArtistClaimsMultiResourceDataDocument.from_dict(artist_claims_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


