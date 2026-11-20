# SearchSuggestionsHistoryMultiRelationshipDataDocument

Target resource types: `searchHistoryEntries`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.search_suggestions_history_multi_relationship_data_document import SearchSuggestionsHistoryMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsHistoryMultiRelationshipDataDocument from a JSON string
search_suggestions_history_multi_relationship_data_document_instance = SearchSuggestionsHistoryMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsHistoryMultiRelationshipDataDocument.to_json())

# convert the object into a dict
search_suggestions_history_multi_relationship_data_document_dict = search_suggestions_history_multi_relationship_data_document_instance.to_dict()
# create an instance of SearchSuggestionsHistoryMultiRelationshipDataDocument from a dict
search_suggestions_history_multi_relationship_data_document_from_dict = SearchSuggestionsHistoryMultiRelationshipDataDocument.from_dict(search_suggestions_history_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


