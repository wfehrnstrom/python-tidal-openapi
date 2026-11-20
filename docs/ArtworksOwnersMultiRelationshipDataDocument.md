# ArtworksOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artworks_owners_multi_relationship_data_document import ArtworksOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksOwnersMultiRelationshipDataDocument from a JSON string
artworks_owners_multi_relationship_data_document_instance = ArtworksOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtworksOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artworks_owners_multi_relationship_data_document_dict = artworks_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtworksOwnersMultiRelationshipDataDocument from a dict
artworks_owners_multi_relationship_data_document_from_dict = ArtworksOwnersMultiRelationshipDataDocument.from_dict(artworks_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


