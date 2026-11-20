# OfflineTasksSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OfflineTasksResourceObject**](OfflineTasksResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.offline_tasks_single_resource_data_document import OfflineTasksSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksSingleResourceDataDocument from a JSON string
offline_tasks_single_resource_data_document_instance = OfflineTasksSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksSingleResourceDataDocument.to_json())

# convert the object into a dict
offline_tasks_single_resource_data_document_dict = offline_tasks_single_resource_data_document_instance.to_dict()
# create an instance of OfflineTasksSingleResourceDataDocument from a dict
offline_tasks_single_resource_data_document_from_dict = OfflineTasksSingleResourceDataDocument.from_dict(offline_tasks_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


