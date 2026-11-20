# CreditsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**CreditsAttributes**](CreditsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**CreditsRelationships**](CreditsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.credits_resource_object import CreditsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsResourceObject from a JSON string
credits_resource_object_instance = CreditsResourceObject.from_json(json)
# print the JSON string representation of the object
print(CreditsResourceObject.to_json())

# convert the object into a dict
credits_resource_object_dict = credits_resource_object_instance.to_dict()
# create an instance of CreditsResourceObject from a dict
credits_resource_object_from_dict = CreditsResourceObject.from_dict(credits_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


