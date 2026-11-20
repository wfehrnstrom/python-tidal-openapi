# UserDiscoveryMixesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserDiscoveryMixesRelationships**](UserDiscoveryMixesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_discovery_mixes_resource_object import UserDiscoveryMixesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserDiscoveryMixesResourceObject from a JSON string
user_discovery_mixes_resource_object_instance = UserDiscoveryMixesResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserDiscoveryMixesResourceObject.to_json())

# convert the object into a dict
user_discovery_mixes_resource_object_dict = user_discovery_mixes_resource_object_instance.to_dict()
# create an instance of UserDiscoveryMixesResourceObject from a dict
user_discovery_mixes_resource_object_from_dict = UserDiscoveryMixesResourceObject.from_dict(user_discovery_mixes_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


