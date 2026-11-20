# SearchSuggestionsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The search query represented by this resource | 
**suggestions** | [**List[SearchSuggestionsSuggestions]**](SearchSuggestionsSuggestions.md) | Suggested search queries | 
**tracking_id** | **str** | Unique tracking id | 

## Example

```python
from tidal.models.search_suggestions_attributes import SearchSuggestionsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsAttributes from a JSON string
search_suggestions_attributes_instance = SearchSuggestionsAttributes.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsAttributes.to_json())

# convert the object into a dict
search_suggestions_attributes_dict = search_suggestions_attributes_instance.to_dict()
# create an instance of SearchSuggestionsAttributes from a dict
search_suggestions_attributes_from_dict = SearchSuggestionsAttributes.from_dict(search_suggestions_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


