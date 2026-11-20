# UserDailyMixesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserDailyMixesResourceObject**](UserDailyMixesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_daily_mixes_single_resource_data_document import UserDailyMixesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserDailyMixesSingleResourceDataDocument from a JSON string
user_daily_mixes_single_resource_data_document_instance = UserDailyMixesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserDailyMixesSingleResourceDataDocument.to_json())

# convert the object into a dict
user_daily_mixes_single_resource_data_document_dict = user_daily_mixes_single_resource_data_document_instance.to_dict()
# create an instance of UserDailyMixesSingleResourceDataDocument from a dict
user_daily_mixes_single_resource_data_document_from_dict = UserDailyMixesSingleResourceDataDocument.from_dict(user_daily_mixes_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


