# UserDataExportsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When the export was requested | 
**data_types** | **List[str]** | Kinds of data the export contains, as picked when requesting it | 
**download_link** | [**LinkObject**](LinkObject.md) |  | [optional] 
**expires_at** | **datetime** | When the export and its download stop being available; absent until it is ready | [optional] 
**ready_at** | **datetime** | When the export became ready; absent until then | [optional] 
**status** | **str** | Lifecycle state of a user data export. New values may be added at any time. | 

## Example

```python
from tidal.models.user_data_exports_attributes import UserDataExportsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsAttributes from a JSON string
user_data_exports_attributes_instance = UserDataExportsAttributes.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsAttributes.to_json())

# convert the object into a dict
user_data_exports_attributes_dict = user_data_exports_attributes_instance.to_dict()
# create an instance of UserDataExportsAttributes from a dict
user_data_exports_attributes_from_dict = UserDataExportsAttributes.from_dict(user_data_exports_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


