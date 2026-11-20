# UserOfflineMixesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserOfflineMixesResourceObject**](UserOfflineMixesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_offline_mixes_single_resource_data_document import UserOfflineMixesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserOfflineMixesSingleResourceDataDocument from a JSON string
user_offline_mixes_single_resource_data_document_instance = UserOfflineMixesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserOfflineMixesSingleResourceDataDocument.to_json())

# convert the object into a dict
user_offline_mixes_single_resource_data_document_dict = user_offline_mixes_single_resource_data_document_instance.to_dict()
# create an instance of UserOfflineMixesSingleResourceDataDocument from a dict
user_offline_mixes_single_resource_data_document_from_dict = UserOfflineMixesSingleResourceDataDocument.from_dict(user_offline_mixes_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


