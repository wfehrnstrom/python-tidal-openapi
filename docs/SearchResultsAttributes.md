# SearchResultsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**did_you_mean** | **str** | &#39;did you mean&#39; prompt | [optional] 
**query** | **str** | The search query represented by this resource | 
**tracking_id** | **str** | search request unique tracking number | 

## Example

```python
from tidal.models.search_results_attributes import SearchResultsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultsAttributes from a JSON string
search_results_attributes_instance = SearchResultsAttributes.from_json(json)
# print the JSON string representation of the object
print(SearchResultsAttributes.to_json())

# convert the object into a dict
search_results_attributes_dict = search_results_attributes_instance.to_dict()
# create an instance of SearchResultsAttributes from a dict
search_results_attributes_from_dict = SearchResultsAttributes.from_dict(search_results_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


