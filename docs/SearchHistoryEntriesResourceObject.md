# SearchHistoryEntriesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SearchHistoryEntriesAttributes**](SearchHistoryEntriesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.search_history_entries_resource_object import SearchHistoryEntriesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SearchHistoryEntriesResourceObject from a JSON string
search_history_entries_resource_object_instance = SearchHistoryEntriesResourceObject.from_json(json)
# print the JSON string representation of the object
print(SearchHistoryEntriesResourceObject.to_json())

# convert the object into a dict
search_history_entries_resource_object_dict = search_history_entries_resource_object_instance.to_dict()
# create an instance of SearchHistoryEntriesResourceObject from a dict
search_history_entries_resource_object_from_dict = SearchHistoryEntriesResourceObject.from_dict(search_history_entries_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


