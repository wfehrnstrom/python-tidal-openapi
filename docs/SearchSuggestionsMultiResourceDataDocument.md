# SearchSuggestionsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SearchSuggestionsResourceObject]**](SearchSuggestionsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.search_suggestions_multi_resource_data_document import SearchSuggestionsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsMultiResourceDataDocument from a JSON string
search_suggestions_multi_resource_data_document_instance = SearchSuggestionsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsMultiResourceDataDocument.to_json())

# convert the object into a dict
search_suggestions_multi_resource_data_document_dict = search_suggestions_multi_resource_data_document_instance.to_dict()
# create an instance of SearchSuggestionsMultiResourceDataDocument from a dict
search_suggestions_multi_resource_data_document_from_dict = SearchSuggestionsMultiResourceDataDocument.from_dict(search_suggestions_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


