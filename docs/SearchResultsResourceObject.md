# SearchResultsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SearchResultsAttributes**](SearchResultsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SearchResultsRelationships**](SearchResultsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.search_results_resource_object import SearchResultsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsResourceObject from a JSON string
search_results_resource_object_instance = SearchResultsResourceObject.from_json(json)
# print the JSON string representation of the object
print(SearchResultsResourceObject.to_json())

# convert the object into a dict
search_results_resource_object_dict = search_results_resource_object_instance.to_dict()
# create an instance of SearchResultsResourceObject from a dict
search_results_resource_object_from_dict = SearchResultsResourceObject.from_dict(search_results_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


