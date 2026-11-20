# ManualArtistClaimsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ManualArtistClaimsResourceObject**](ManualArtistClaimsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.manual_artist_claims_create_single_resource_data_document import ManualArtistClaimsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ManualArtistClaimsCreateSingleResourceDataDocument from a JSON string
manual_artist_claims_create_single_resource_data_document_instance = ManualArtistClaimsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ManualArtistClaimsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
manual_artist_claims_create_single_resource_data_document_dict = manual_artist_claims_create_single_resource_data_document_instance.to_dict()
# create an instance of ManualArtistClaimsCreateSingleResourceDataDocument from a dict
manual_artist_claims_create_single_resource_data_document_from_dict = ManualArtistClaimsCreateSingleResourceDataDocument.from_dict(manual_artist_claims_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


