# DrmData

DRM data. Absence implies no DRM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_url** | **str** |  | [optional] 
**drm_system** | **str** |  | [optional] 
**init_data** | **List[str]** |  | [optional] 
**license_url** | **str** |  | [optional] 

## Example

```python
from tidal.models.drm_data import DrmData

# TODO update the JSON string below
json = "{}"
# create an instance of DrmData from a JSON string
drm_data_instance = DrmData.from_json(json)
# print the JSON string representation of the object
print(DrmData.to_json())

# convert the object into a dict
drm_data_dict = drm_data_instance.to_dict()
# create an instance of DrmData from a dict
drm_data_from_dict = DrmData.from_dict(drm_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


