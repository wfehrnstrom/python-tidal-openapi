# SearchResultsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SearchResultsResourceObject]**](SearchResultsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.search_results_multi_resource_data_document import SearchResultsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsMultiResourceDataDocument from a JSON string
search_results_multi_resource_data_document_instance = SearchResultsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SearchResultsMultiResourceDataDocument.to_json())

# convert the object into a dict
search_results_multi_resource_data_document_dict = search_results_multi_resource_data_document_instance.to_dict()
# create an instance of SearchResultsMultiResourceDataDocument from a dict
search_results_multi_resource_data_document_from_dict = SearchResultsMultiResourceDataDocument.from_dict(search_results_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


