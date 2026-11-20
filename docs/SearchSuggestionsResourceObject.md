# SearchSuggestionsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SearchSuggestionsAttributes**](SearchSuggestionsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SearchSuggestionsRelationships**](SearchSuggestionsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.search_suggestions_resource_object import SearchSuggestionsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSuggestionsResourceObject from a JSON string
search_suggestions_resource_object_instance = SearchSuggestionsResourceObject.from_json(json)
# print the JSON string representation of the object
print(SearchSuggestionsResourceObject.to_json())

# convert the object into a dict
search_suggestions_resource_object_dict = search_suggestions_resource_object_instance.to_dict()
# create an instance of SearchSuggestionsResourceObject from a dict
search_suggestions_resource_object_from_dict = SearchSuggestionsResourceObject.from_dict(search_suggestions_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


