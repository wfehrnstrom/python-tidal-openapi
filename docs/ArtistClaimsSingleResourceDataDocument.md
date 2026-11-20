# ArtistClaimsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistClaimsResourceObject**](ArtistClaimsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_claims_single_resource_data_document import ArtistClaimsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsSingleResourceDataDocument from a JSON string
artist_claims_single_resource_data_document_instance = ArtistClaimsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsSingleResourceDataDocument.to_json())

# convert the object into a dict
artist_claims_single_resource_data_document_dict = artist_claims_single_resource_data_document_instance.to_dict()
# create an instance of ArtistClaimsSingleResourceDataDocument from a dict
artist_claims_single_resource_data_document_from_dict = ArtistClaimsSingleResourceDataDocument.from_dict(artist_claims_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


