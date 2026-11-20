# ResourceGrantsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ResourceGrantsAttributes**](ResourceGrantsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ResourceGrantsRelationships**](ResourceGrantsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.resource_grants_resource_object import ResourceGrantsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsResourceObject from a JSON string
resource_grants_resource_object_instance = ResourceGrantsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsResourceObject.to_json())

# convert the object into a dict
resource_grants_resource_object_dict = resource_grants_resource_object_instance.to_dict()
# create an instance of ResourceGrantsResourceObject from a dict
resource_grants_resource_object_from_dict = ResourceGrantsResourceObject.from_dict(resource_grants_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


