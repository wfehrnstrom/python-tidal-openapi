# ArtistClaimStatusesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistClaimStatusesResourceObject]**](ArtistClaimStatusesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artist_claim_statuses_multi_resource_data_document import ArtistClaimStatusesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistClaimStatusesMultiResourceDataDocument from a JSON string
artist_claim_statuses_multi_resource_data_document_instance = ArtistClaimStatusesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistClaimStatusesMultiResourceDataDocument.to_json())

# convert the object into a dict
artist_claim_statuses_multi_resource_data_document_dict = artist_claim_statuses_multi_resource_data_document_instance.to_dict()
# create an instance of ArtistClaimStatusesMultiResourceDataDocument from a dict
artist_claim_statuses_multi_resource_data_document_from_dict = ArtistClaimStatusesMultiResourceDataDocument.from_dict(artist_claim_statuses_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


