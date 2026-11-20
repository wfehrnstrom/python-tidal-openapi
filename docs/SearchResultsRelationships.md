# SearchResultsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**SearchResultsAlbumsMultiRelationshipDataDocument**](SearchResultsAlbumsMultiRelationshipDataDocument.md) |  | [optional] 
**artists** | [**SearchResultsArtistsMultiRelationshipDataDocument**](SearchResultsArtistsMultiRelationshipDataDocument.md) |  | [optional] 
**playlists** | [**SearchResultsPlaylistsMultiRelationshipDataDocument**](SearchResultsPlaylistsMultiRelationshipDataDocument.md) |  | [optional] 
**top_hits** | [**SearchResultsTopHitsMultiRelationshipDataDocument**](SearchResultsTopHitsMultiRelationshipDataDocument.md) |  | [optional] 
**tracks** | [**SearchResultsTracksMultiRelationshipDataDocument**](SearchResultsTracksMultiRelationshipDataDocument.md) |  | [optional] 
**videos** | [**SearchResultsVideosMultiRelationshipDataDocument**](SearchResultsVideosMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.search_results_relationships import SearchResultsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsRelationships from a JSON string
search_results_relationships_instance = SearchResultsRelationships.from_json(json)
# print the JSON string representation of the object
print(SearchResultsRelationships.to_json())

# convert the object into a dict
search_results_relationships_dict = search_results_relationships_instance.to_dict()
# create an instance of SearchResultsRelationships from a dict
search_results_relationships_from_dict = SearchResultsRelationships.from_dict(search_results_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


