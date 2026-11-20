# UserNewReleaseMixesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserNewReleaseMixesResourceObject**](UserNewReleaseMixesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_new_release_mixes_single_resource_data_document import UserNewReleaseMixesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserNewReleaseMixesSingleResourceDataDocument from a JSON string
user_new_release_mixes_single_resource_data_document_instance = UserNewReleaseMixesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserNewReleaseMixesSingleResourceDataDocument.to_json())

# convert the object into a dict
user_new_release_mixes_single_resource_data_document_dict = user_new_release_mixes_single_resource_data_document_instance.to_dict()
# create an instance of UserNewReleaseMixesSingleResourceDataDocument from a dict
user_new_release_mixes_single_resource_data_document_from_dict = UserNewReleaseMixesSingleResourceDataDocument.from_dict(user_new_release_mixes_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


