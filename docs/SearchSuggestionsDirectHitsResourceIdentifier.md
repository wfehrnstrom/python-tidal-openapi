# SearchSuggestionsDirectHitsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**SearchSuggestionsDirectHitsResourceIdentifierMeta**](SearchSuggestionsDirectHitsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.search_suggestions_direct_hits_resource_identifier import SearchSuggestionsDirectHitsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsDirectHitsResourceIdentifier from a JSON string
search_suggestions_direct_hits_resource_identifier_instance = SearchSuggestionsDirectHitsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsDirectHitsResourceIdentifier.to_json())

# convert the object into a dict
search_suggestions_direct_hits_resource_identifier_dict = search_suggestions_direct_hits_resource_identifier_instance.to_dict()
# create an instance of SearchSuggestionsDirectHitsResourceIdentifier from a dict
search_suggestions_direct_hits_resource_identifier_from_dict = SearchSuggestionsDirectHitsResourceIdentifier.from_dict(search_suggestions_direct_hits_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


