# SearchSuggestionsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_hits** | [**SearchSuggestionsDirectHitsMultiRelationshipDataDocument**](SearchSuggestionsDirectHitsMultiRelationshipDataDocument.md) |  | [optional] 
**history** | [**SearchSuggestionsHistoryMultiRelationshipDataDocument**](SearchSuggestionsHistoryMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.search_suggestions_relationships import SearchSuggestionsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsRelationships from a JSON string
search_suggestions_relationships_instance = SearchSuggestionsRelationships.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsRelationships.to_json())

# convert the object into a dict
search_suggestions_relationships_dict = search_suggestions_relationships_instance.to_dict()
# create an instance of SearchSuggestionsRelationships from a dict
search_suggestions_relationships_from_dict = SearchSuggestionsRelationships.from_dict(search_suggestions_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


