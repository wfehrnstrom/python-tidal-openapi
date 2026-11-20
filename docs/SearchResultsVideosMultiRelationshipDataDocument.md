# SearchResultsVideosMultiRelationshipDataDocument

Target resource types: `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SearchResultsVideosResourceIdentifier]**](SearchResultsVideosResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.search_results_videos_multi_relationship_data_document import SearchResultsVideosMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsVideosMultiRelationshipDataDocument from a JSON string
search_results_videos_multi_relationship_data_document_instance = SearchResultsVideosMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SearchResultsVideosMultiRelationshipDataDocument.to_json())

# convert the object into a dict
search_results_videos_multi_relationship_data_document_dict = search_results_videos_multi_relationship_data_document_instance.to_dict()
# create an instance of SearchResultsVideosMultiRelationshipDataDocument from a dict
search_results_videos_multi_relationship_data_document_from_dict = SearchResultsVideosMultiRelationshipDataDocument.from_dict(search_results_videos_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


