# UserDataExportRequestsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserDataExportRequestsResourceObject**](UserDataExportRequestsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_data_export_requests_create_single_resource_data_document import UserDataExportRequestsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportRequestsCreateSingleResourceDataDocument from a JSON string
user_data_export_requests_create_single_resource_data_document_instance = UserDataExportRequestsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserDataExportRequestsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
user_data_export_requests_create_single_resource_data_document_dict = user_data_export_requests_create_single_resource_data_document_instance.to_dict()
# create an instance of UserDataExportRequestsCreateSingleResourceDataDocument from a dict
user_data_export_requests_create_single_resource_data_document_from_dict = UserDataExportRequestsCreateSingleResourceDataDocument.from_dict(user_data_export_requests_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


