# SearchResultsAlbumsResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**SearchResultsAlbumsResourceIdentifierMeta**](SearchResultsAlbumsResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.search_results_albums_resource_identifier import SearchResultsAlbumsResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsAlbumsResourceIdentifier from a JSON string
search_results_albums_resource_identifier_instance = SearchResultsAlbumsResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(SearchResultsAlbumsResourceIdentifier.to_json())

# convert the object into a dict
search_results_albums_resource_identifier_dict = search_results_albums_resource_identifier_instance.to_dict()
# create an instance of SearchResultsAlbumsResourceIdentifier from a dict
search_results_albums_resource_identifier_from_dict = SearchResultsAlbumsResourceIdentifier.from_dict(search_results_albums_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


