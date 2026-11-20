# DspSharingLinksResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DspSharingLinksAttributes**](DspSharingLinksAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**DspSharingLinksRelationships**](DspSharingLinksRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.dsp_sharing_links_resource_object import DspSharingLinksResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DspSharingLinksResourceObject from a JSON string
dsp_sharing_links_resource_object_instance = DspSharingLinksResourceObject.from_json(json)
# print the JSON string representation of the object
print(DspSharingLinksResourceObject.to_json())

# convert the object into a dict
dsp_sharing_links_resource_object_dict = dsp_sharing_links_resource_object_instance.to_dict()
# create an instance of DspSharingLinksResourceObject from a dict
dsp_sharing_links_resource_object_from_dict = DspSharingLinksResourceObject.from_dict(dsp_sharing_links_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


