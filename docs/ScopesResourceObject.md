# ScopesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ScopesAttributes**](ScopesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.scopes_resource_object import ScopesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ScopesResourceObject from a JSON string
scopes_resource_object_instance = ScopesResourceObject.from_json(json)
# print the JSON string representation of the object
print(ScopesResourceObject.to_json())

# convert the object into a dict
scopes_resource_object_dict = scopes_resource_object_instance.to_dict()
# create an instance of ScopesResourceObject from a dict
scopes_resource_object_from_dict = ScopesResourceObject.from_dict(scopes_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


