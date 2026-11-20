# TemporaryUserTokensResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**TemporaryUserTokensRelationships**](TemporaryUserTokensRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.temporary_user_tokens_resource_object import TemporaryUserTokensResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryUserTokensResourceObject from a JSON string
temporary_user_tokens_resource_object_instance = TemporaryUserTokensResourceObject.from_json(json)
# print the JSON string representation of the object
print(TemporaryUserTokensResourceObject.to_json())

# convert the object into a dict
temporary_user_tokens_resource_object_dict = temporary_user_tokens_resource_object_instance.to_dict()
# create an instance of TemporaryUserTokensResourceObject from a dict
temporary_user_tokens_resource_object_from_dict = TemporaryUserTokensResourceObject.from_dict(temporary_user_tokens_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


