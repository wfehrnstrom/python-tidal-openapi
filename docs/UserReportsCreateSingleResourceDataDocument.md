# UserReportsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserReportsResourceObject**](UserReportsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_reports_create_single_resource_data_document import UserReportsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserReportsCreateSingleResourceDataDocument from a JSON string
user_reports_create_single_resource_data_document_instance = UserReportsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserReportsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
user_reports_create_single_resource_data_document_dict = user_reports_create_single_resource_data_document_instance.to_dict()
# create an instance of UserReportsCreateSingleResourceDataDocument from a dict
user_reports_create_single_resource_data_document_from_dict = UserReportsCreateSingleResourceDataDocument.from_dict(user_reports_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


