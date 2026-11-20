# SearchSuggestionsSuggestions

Suggested search queries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlights** | [**List[SearchSuggestionsHighlights]**](SearchSuggestionsHighlights.md) | Ranges in &#x60;query&#x60; that clients should highlight as matches for the requested search query | 
**query** | **str** | The suggested search query | 

## Example

```python
from tidal.models.search_suggestions_suggestions import SearchSuggestionsSuggestions

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsSuggestions from a JSON string
search_suggestions_suggestions_instance = SearchSuggestionsSuggestions.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsSuggestions.to_json())

# convert the object into a dict
search_suggestions_suggestions_dict = search_suggestions_suggestions_instance.to_dict()
# create an instance of SearchSuggestionsSuggestions from a dict
search_suggestions_suggestions_from_dict = SearchSuggestionsSuggestions.from_dict(search_suggestions_suggestions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


