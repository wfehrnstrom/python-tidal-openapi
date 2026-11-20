# SearchResultsAlbumsResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.search_results_albums_resource_identifier_meta import SearchResultsAlbumsResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsAlbumsResourceIdentifierMeta from a JSON string
search_results_albums_resource_identifier_meta_instance = SearchResultsAlbumsResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(SearchResultsAlbumsResourceIdentifierMeta.to_json())

# convert the object into a dict
search_results_albums_resource_identifier_meta_dict = search_results_albums_resource_identifier_meta_instance.to_dict()
# create an instance of SearchResultsAlbumsResourceIdentifierMeta from a dict
search_results_albums_resource_identifier_meta_from_dict = SearchResultsAlbumsResourceIdentifierMeta.from_dict(search_results_albums_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


