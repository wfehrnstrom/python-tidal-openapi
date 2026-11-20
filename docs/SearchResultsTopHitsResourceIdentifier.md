# SearchResultsTopHitsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**SearchResultsTopHitsResourceIdentifierMeta**](SearchResultsTopHitsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.search_results_top_hits_resource_identifier import SearchResultsTopHitsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsTopHitsResourceIdentifier from a JSON string
search_results_top_hits_resource_identifier_instance = SearchResultsTopHitsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(SearchResultsTopHitsResourceIdentifier.to_json())

# convert the object into a dict
search_results_top_hits_resource_identifier_dict = search_results_top_hits_resource_identifier_instance.to_dict()
# create an instance of SearchResultsTopHitsResourceIdentifier from a dict
search_results_top_hits_resource_identifier_from_dict = SearchResultsTopHitsResourceIdentifier.from_dict(search_results_top_hits_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


