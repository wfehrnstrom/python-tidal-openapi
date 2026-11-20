# LyricsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.lyrics_owners_multi_relationship_data_document import LyricsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsOwnersMultiRelationshipDataDocument from a JSON string
lyrics_owners_multi_relationship_data_document_instance = LyricsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(LyricsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
lyrics_owners_multi_relationship_data_document_dict = lyrics_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of LyricsOwnersMultiRelationshipDataDocument from a dict
lyrics_owners_multi_relationship_data_document_from_dict = LyricsOwnersMultiRelationshipDataDocument.from_dict(lyrics_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


