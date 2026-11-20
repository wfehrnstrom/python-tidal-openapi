# UserDataExportsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserDataExportsResourceObject**](UserDataExportsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_data_exports_create_single_resource_data_document import UserDataExportsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsCreateSingleResourceDataDocument from a JSON string
user_data_exports_create_single_resource_data_document_instance = UserDataExportsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
user_data_exports_create_single_resource_data_document_dict = user_data_exports_create_single_resource_data_document_instance.to_dict()
# create an instance of UserDataExportsCreateSingleResourceDataDocument from a dict
user_data_exports_create_single_resource_data_document_from_dict = UserDataExportsCreateSingleResourceDataDocument.from_dict(user_data_exports_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


