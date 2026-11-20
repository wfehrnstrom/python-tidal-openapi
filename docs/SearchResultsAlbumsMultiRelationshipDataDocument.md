# SearchResultsAlbumsMultiRelationshipDataDocument

Target resource types: `albums`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SearchResultsAlbumsResourceIdentifier]**](SearchResultsAlbumsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.search_results_albums_multi_relationship_data_document import SearchResultsAlbumsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsAlbumsMultiRelationshipDataDocument from a JSON string
search_results_albums_multi_relationship_data_document_instance = SearchResultsAlbumsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SearchResultsAlbumsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
search_results_albums_multi_relationship_data_document_dict = search_results_albums_multi_relationship_data_document_instance.to_dict()
# create an instance of SearchResultsAlbumsMultiRelationshipDataDocument from a dict
search_results_albums_multi_relationship_data_document_from_dict = SearchResultsAlbumsMultiRelationshipDataDocument.from_dict(search_results_albums_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


