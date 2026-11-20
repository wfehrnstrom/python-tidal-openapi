# ArtistsBiographySingleRelationshipDataDocument

Target resource types: `artistBiographies`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_biography_single_relationship_data_document import ArtistsBiographySingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsBiographySingleRelationshipDataDocument from a JSON string
artists_biography_single_relationship_data_document_instance = ArtistsBiographySingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsBiographySingleRelationshipDataDocument.to_json())

# convert the object into a dict
artists_biography_single_relationship_data_document_dict = artists_biography_single_relationship_data_document_instance.to_dict()
# create an instance of ArtistsBiographySingleRelationshipDataDocument from a dict
artists_biography_single_relationship_data_document_from_dict = ArtistsBiographySingleRelationshipDataDocument.from_dict(artists_biography_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


