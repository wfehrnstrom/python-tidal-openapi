# GenresResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**GenresAttributes**](GenresAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.genres_resource_object import GenresResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of GenresResourceObject from a JSON string
genres_resource_object_instance = GenresResourceObject.from_json(json)
# print the JSON string representation of the object
print(GenresResourceObject.to_json())

# convert the object into a dict
genres_resource_object_dict = genres_resource_object_instance.to_dict()
# create an instance of GenresResourceObject from a dict
genres_resource_object_from_dict = GenresResourceObject.from_dict(genres_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


