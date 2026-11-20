# SearchSuggestionsHighlights


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Length of the highlight range, measured in UTF-16 code units | 
**start** | **int** | Zero-based start offset in the suggested query, measured in UTF-16 code units | 

## Example

```python
from tidal.models.search_suggestions_highlights import SearchSuggestionsHighlights

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsHighlights from a JSON string
search_suggestions_highlights_instance = SearchSuggestionsHighlights.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsHighlights.to_json())

# convert the object into a dict
search_suggestions_highlights_dict = search_suggestions_highlights_instance.to_dict()
# create an instance of SearchSuggestionsHighlights from a dict
search_suggestions_highlights_from_dict = SearchSuggestionsHighlights.from_dict(search_suggestions_highlights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


