# ArtistsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_owners_multi_relationship_data_document import ArtistsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsOwnersMultiRelationshipDataDocument from a JSON string
artists_owners_multi_relationship_data_document_instance = ArtistsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_owners_multi_relationship_data_document_dict = artists_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsOwnersMultiRelationshipDataDocument from a dict
artists_owners_multi_relationship_data_document_from_dict = ArtistsOwnersMultiRelationshipDataDocument.from_dict(artists_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


