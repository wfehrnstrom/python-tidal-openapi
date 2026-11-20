# CreditsArtistSingleRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.credits_artist_single_relationship_data_document import CreditsArtistSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsArtistSingleRelationshipDataDocument from a JSON string
credits_artist_single_relationship_data_document_instance = CreditsArtistSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(CreditsArtistSingleRelationshipDataDocument.to_json())

# convert the object into a dict
credits_artist_single_relationship_data_document_dict = credits_artist_single_relationship_data_document_instance.to_dict()
# create an instance of CreditsArtistSingleRelationshipDataDocument from a dict
credits_artist_single_relationship_data_document_from_dict = CreditsArtistSingleRelationshipDataDocument.from_dict(credits_artist_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


