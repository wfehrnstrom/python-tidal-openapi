# AppreciationsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**AppreciationsAttributes**](AppreciationsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.appreciations_resource_object import AppreciationsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of AppreciationsResourceObject from a JSON string
appreciations_resource_object_instance = AppreciationsResourceObject.from_json(json)
# print the JSON string representation of the object
print(AppreciationsResourceObject.to_json())

# convert the object into a dict
appreciations_resource_object_dict = appreciations_resource_object_instance.to_dict()
# create an instance of AppreciationsResourceObject from a dict
appreciations_resource_object_from_dict = AppreciationsResourceObject.from_dict(appreciations_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


