# ResourceObjectObjectObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | **object** |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.resource_object_object_object import ResourceObjectObjectObject

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceObjectObjectObject from a JSON string
resource_object_object_object_instance = ResourceObjectObjectObject.from_json(json)
# print the JSON string representation of the object
print(ResourceObjectObjectObject.to_json())

# convert the object into a dict
resource_object_object_object_dict = resource_object_object_object_instance.to_dict()
# create an instance of ResourceObjectObjectObject from a dict
resource_object_object_object_from_dict = ResourceObjectObjectObject.from_dict(resource_object_object_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


