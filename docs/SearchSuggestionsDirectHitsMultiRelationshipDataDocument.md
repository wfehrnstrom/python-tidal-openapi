# SearchSuggestionsDirectHitsMultiRelationshipDataDocument

Target resource types: `albums`, `artists`, `playlists`, `tracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SearchSuggestionsDirectHitsResourceIdentifier]**](SearchSuggestionsDirectHitsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.search_suggestions_direct_hits_multi_relationship_data_document import SearchSuggestionsDirectHitsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsDirectHitsMultiRelationshipDataDocument from a JSON string
search_suggestions_direct_hits_multi_relationship_data_document_instance = SearchSuggestionsDirectHitsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsDirectHitsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
search_suggestions_direct_hits_multi_relationship_data_document_dict = search_suggestions_direct_hits_multi_relationship_data_document_instance.to_dict()
# create an instance of SearchSuggestionsDirectHitsMultiRelationshipDataDocument from a dict
search_suggestions_direct_hits_multi_relationship_data_document_from_dict = SearchSuggestionsDirectHitsMultiRelationshipDataDocument.from_dict(search_suggestions_direct_hits_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


