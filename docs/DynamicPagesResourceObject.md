# DynamicPagesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DynamicPagesAttributes**](DynamicPagesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**DynamicPagesRelationships**](DynamicPagesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.dynamic_pages_resource_object import DynamicPagesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPagesResourceObject from a JSON string
dynamic_pages_resource_object_instance = DynamicPagesResourceObject.from_json(json)
# print the JSON string representation of the object
print(DynamicPagesResourceObject.to_json())

# convert the object into a dict
dynamic_pages_resource_object_dict = dynamic_pages_resource_object_instance.to_dict()
# create an instance of DynamicPagesResourceObject from a dict
dynamic_pages_resource_object_from_dict = DynamicPagesResourceObject.from_dict(dynamic_pages_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


