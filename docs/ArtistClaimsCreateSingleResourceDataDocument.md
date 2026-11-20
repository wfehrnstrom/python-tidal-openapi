# ArtistClaimsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArtistClaimsResourceObject**](ArtistClaimsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_claims_create_single_resource_data_document import ArtistClaimsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimsCreateSingleResourceDataDocument from a JSON string
artist_claims_create_single_resource_data_document_instance = ArtistClaimsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
artist_claims_create_single_resource_data_document_dict = artist_claims_create_single_resource_data_document_instance.to_dict()
# create an instance of ArtistClaimsCreateSingleResourceDataDocument from a dict
artist_claims_create_single_resource_data_document_from_dict = ArtistClaimsCreateSingleResourceDataDocument.from_dict(artist_claims_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


