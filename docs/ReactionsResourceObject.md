# ReactionsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ReactionsAttributes**](ReactionsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ReactionsRelationships**](ReactionsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.reactions_resource_object import ReactionsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsResourceObject from a JSON string
reactions_resource_object_instance = ReactionsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ReactionsResourceObject.to_json())

# convert the object into a dict
reactions_resource_object_dict = reactions_resource_object_instance.to_dict()
# create an instance of ReactionsResourceObject from a dict
reactions_resource_object_from_dict = ReactionsResourceObject.from_dict(reactions_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


