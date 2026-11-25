# StudioHomeInsightTilesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**StudioHomeInsightTilesAttributes**](StudioHomeInsightTilesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**StudioHomeInsightTilesRelationships**](StudioHomeInsightTilesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.studio_home_insight_tiles_resource_object import StudioHomeInsightTilesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeInsightTilesResourceObject from a JSON string
studio_home_insight_tiles_resource_object_instance = StudioHomeInsightTilesResourceObject.from_json(json)
# print the JSON string representation of the object
print(StudioHomeInsightTilesResourceObject.to_json())

# convert the object into a dict
studio_home_insight_tiles_resource_object_dict = studio_home_insight_tiles_resource_object_instance.to_dict()
# create an instance of StudioHomeInsightTilesResourceObject from a dict
studio_home_insight_tiles_resource_object_from_dict = StudioHomeInsightTilesResourceObject.from_dict(studio_home_insight_tiles_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


