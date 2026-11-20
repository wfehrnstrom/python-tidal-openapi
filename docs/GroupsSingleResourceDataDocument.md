# GroupsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupsResourceObject**](GroupsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.groups_single_resource_data_document import GroupsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsSingleResourceDataDocument from a JSON string
groups_single_resource_data_document_instance = GroupsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(GroupsSingleResourceDataDocument.to_json())

# convert the object into a dict
groups_single_resource_data_document_dict = groups_single_resource_data_document_instance.to_dict()
# create an instance of GroupsSingleResourceDataDocument from a dict
groups_single_resource_data_document_from_dict = GroupsSingleResourceDataDocument.from_dict(groups_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


