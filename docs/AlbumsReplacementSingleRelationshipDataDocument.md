# AlbumsReplacementSingleRelationshipDataDocument

Target resource types: `albums`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlbumsReplacementResourceIdentifier**](AlbumsReplacementResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_replacement_single_relationship_data_document import AlbumsReplacementSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsReplacementSingleRelationshipDataDocument from a JSON string
albums_replacement_single_relationship_data_document_instance = AlbumsReplacementSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsReplacementSingleRelationshipDataDocument.to_json())

# convert the object into a dict
albums_replacement_single_relationship_data_document_dict = albums_replacement_single_relationship_data_document_instance.to_dict()
# create an instance of AlbumsReplacementSingleRelationshipDataDocument from a dict
albums_replacement_single_relationship_data_document_from_dict = AlbumsReplacementSingleRelationshipDataDocument.from_dict(albums_replacement_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


