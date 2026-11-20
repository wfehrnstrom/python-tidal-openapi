# SearchResultsTracksResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**SearchResultsTracksResourceIdentifierMeta**](SearchResultsTracksResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.search_results_tracks_resource_identifier import SearchResultsTracksResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsTracksResourceIdentifier from a JSON string
search_results_tracks_resource_identifier_instance = SearchResultsTracksResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(SearchResultsTracksResourceIdentifier.to_json())

# convert the object into a dict
search_results_tracks_resource_identifier_dict = search_results_tracks_resource_identifier_instance.to_dict()
# create an instance of SearchResultsTracksResourceIdentifier from a dict
search_results_tracks_resource_identifier_from_dict = SearchResultsTracksResourceIdentifier.from_dict(search_results_tracks_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


