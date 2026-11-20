# StudioHomeMerchTilesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**StudioHomeMerchTilesAttributes**](StudioHomeMerchTilesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**StudioHomeMerchTilesRelationships**](StudioHomeMerchTilesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.studio_home_merch_tiles_resource_object import StudioHomeMerchTilesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeMerchTilesResourceObject from a JSON string
studio_home_merch_tiles_resource_object_instance = StudioHomeMerchTilesResourceObject.from_json(json)
# print the JSON string representation of the object
print(StudioHomeMerchTilesResourceObject.to_json())

# convert the object into a dict
studio_home_merch_tiles_resource_object_dict = studio_home_merch_tiles_resource_object_instance.to_dict()
# create an instance of StudioHomeMerchTilesResourceObject from a dict
studio_home_merch_tiles_resource_object_from_dict = StudioHomeMerchTilesResourceObject.from_dict(studio_home_merch_tiles_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


