# ProvidersResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ProvidersAttributes**](ProvidersAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.providers_resource_object import ProvidersResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersResourceObject from a JSON string
providers_resource_object_instance = ProvidersResourceObject.from_json(json)
# print the JSON string representation of the object
print(ProvidersResourceObject.to_json())

# convert the object into a dict
providers_resource_object_dict = providers_resource_object_instance.to_dict()
# create an instance of ProvidersResourceObject from a dict
providers_resource_object_from_dict = ProvidersResourceObject.from_dict(providers_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


