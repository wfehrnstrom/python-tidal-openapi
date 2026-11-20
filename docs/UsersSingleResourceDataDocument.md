# UsersSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsersResourceObject**](UsersResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.users_single_resource_data_document import UsersSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSingleResourceDataDocument from a JSON string
users_single_resource_data_document_instance = UsersSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UsersSingleResourceDataDocument.to_json())

# convert the object into a dict
users_single_resource_data_document_dict = users_single_resource_data_document_instance.to_dict()
# create an instance of UsersSingleResourceDataDocument from a dict
users_single_resource_data_document_from_dict = UsersSingleResourceDataDocument.from_dict(users_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


