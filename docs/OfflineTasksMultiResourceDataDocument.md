# OfflineTasksMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OfflineTasksResourceObject]**](OfflineTasksResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.offline_tasks_multi_resource_data_document import OfflineTasksMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineTasksMultiResourceDataDocument from a JSON string
offline_tasks_multi_resource_data_document_instance = OfflineTasksMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(OfflineTasksMultiResourceDataDocument.to_json())

# convert the object into a dict
offline_tasks_multi_resource_data_document_dict = offline_tasks_multi_resource_data_document_instance.to_dict()
# create an instance of OfflineTasksMultiResourceDataDocument from a dict
offline_tasks_multi_resource_data_document_from_dict = OfflineTasksMultiResourceDataDocument.from_dict(offline_tasks_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


