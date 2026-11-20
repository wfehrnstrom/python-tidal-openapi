# SearchResultsTopHitsMultiRelationshipDataDocument

Target resource types: `albums`, `artists`, `playlists`, `tracks`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SearchResultsTopHitsResourceIdentifier]**](SearchResultsTopHitsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.search_results_top_hits_multi_relationship_data_document import SearchResultsTopHitsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsTopHitsMultiRelationshipDataDocument from a JSON string
search_results_top_hits_multi_relationship_data_document_instance = SearchResultsTopHitsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SearchResultsTopHitsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
search_results_top_hits_multi_relationship_data_document_dict = search_results_top_hits_multi_relationship_data_document_instance.to_dict()
# create an instance of SearchResultsTopHitsMultiRelationshipDataDocument from a dict
search_results_top_hits_multi_relationship_data_document_from_dict = SearchResultsTopHitsMultiRelationshipDataDocument.from_dict(search_results_top_hits_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


