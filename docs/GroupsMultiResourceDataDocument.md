# GroupsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GroupsResourceObject]**](GroupsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.groups_multi_resource_data_document import GroupsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsMultiResourceDataDocument from a JSON string
groups_multi_resource_data_document_instance = GroupsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(GroupsMultiResourceDataDocument.to_json())

# convert the object into a dict
groups_multi_resource_data_document_dict = groups_multi_resource_data_document_instance.to_dict()
# create an instance of GroupsMultiResourceDataDocument from a dict
groups_multi_resource_data_document_from_dict = GroupsMultiResourceDataDocument.from_dict(groups_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


