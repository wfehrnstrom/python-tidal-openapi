# SquareSitesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareSitesAttributes**](SquareSitesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SquareSitesRelationships**](SquareSitesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.square_sites_resource_object import SquareSitesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SquareSitesResourceObject from a JSON string
square_sites_resource_object_instance = SquareSitesResourceObject.from_json(json)
# print the JSON string representation of the object
print(SquareSitesResourceObject.to_json())

# convert the object into a dict
square_sites_resource_object_dict = square_sites_resource_object_instance.to_dict()
# create an instance of SquareSitesResourceObject from a dict
square_sites_resource_object_from_dict = SquareSitesResourceObject.from_dict(square_sites_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


