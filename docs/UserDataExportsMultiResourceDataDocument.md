# UserDataExportsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserDataExportsResourceObject]**](UserDataExportsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_data_exports_multi_resource_data_document import UserDataExportsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsMultiResourceDataDocument from a JSON string
user_data_exports_multi_resource_data_document_instance = UserDataExportsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsMultiResourceDataDocument.to_json())

# convert the object into a dict
user_data_exports_multi_resource_data_document_dict = user_data_exports_multi_resource_data_document_instance.to_dict()
# create an instance of UserDataExportsMultiResourceDataDocument from a dict
user_data_exports_multi_resource_data_document_from_dict = UserDataExportsMultiResourceDataDocument.from_dict(user_data_exports_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


