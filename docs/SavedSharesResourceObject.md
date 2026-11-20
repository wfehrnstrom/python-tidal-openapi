# SavedSharesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SavedSharesAttributes**](SavedSharesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.saved_shares_resource_object import SavedSharesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSharesResourceObject from a JSON string
saved_shares_resource_object_instance = SavedSharesResourceObject.from_json(json)
# print the JSON string representation of the object
print(SavedSharesResourceObject.to_json())

# convert the object into a dict
saved_shares_resource_object_dict = saved_shares_resource_object_instance.to_dict()
# create an instance of SavedSharesResourceObject from a dict
saved_shares_resource_object_from_dict = SavedSharesResourceObject.from_dict(saved_shares_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


