# SearchResultsPlaylistsMultiRelationshipDataDocument

Target resource types: `playlists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.search_results_playlists_multi_relationship_data_document import SearchResultsPlaylistsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsPlaylistsMultiRelationshipDataDocument from a JSON string
search_results_playlists_multi_relationship_data_document_instance = SearchResultsPlaylistsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SearchResultsPlaylistsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
search_results_playlists_multi_relationship_data_document_dict = search_results_playlists_multi_relationship_data_document_instance.to_dict()
# create an instance of SearchResultsPlaylistsMultiRelationshipDataDocument from a dict
search_results_playlists_multi_relationship_data_document_from_dict = SearchResultsPlaylistsMultiRelationshipDataDocument.from_dict(search_results_playlists_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


