# SearchResultsVideosResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**SearchResultsVideosResourceIdentifierMeta**](SearchResultsVideosResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.search_results_videos_resource_identifier import SearchResultsVideosResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsVideosResourceIdentifier from a JSON string
search_results_videos_resource_identifier_instance = SearchResultsVideosResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(SearchResultsVideosResourceIdentifier.to_json())

# convert the object into a dict
search_results_videos_resource_identifier_dict = search_results_videos_resource_identifier_instance.to_dict()
# create an instance of SearchResultsVideosResourceIdentifier from a dict
search_results_videos_resource_identifier_from_dict = SearchResultsVideosResourceIdentifier.from_dict(search_results_videos_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


