# InstallationsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**InstallationsAttributes**](InstallationsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**InstallationsRelationships**](InstallationsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.installations_resource_object import InstallationsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsResourceObject from a JSON string
installations_resource_object_instance = InstallationsResourceObject.from_json(json)
# print the JSON string representation of the object
print(InstallationsResourceObject.to_json())

# convert the object into a dict
installations_resource_object_dict = installations_resource_object_instance.to_dict()
# create an instance of InstallationsResourceObject from a dict
installations_resource_object_from_dict = InstallationsResourceObject.from_dict(installations_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


