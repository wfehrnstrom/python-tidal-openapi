# DspSharingLinksAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_music** | [**LinkObject**](LinkObject.md) |  | [optional] 
**apple_music** | [**LinkObject**](LinkObject.md) |  | [optional] 
**spotify** | [**LinkObject**](LinkObject.md) |  | [optional] 
**you_tube_music** | [**LinkObject**](LinkObject.md) |  | [optional] 

## Example

```python
from tidal.models.dsp_sharing_links_attributes import DspSharingLinksAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DspSharingLinksAttributes from a JSON string
dsp_sharing_links_attributes_instance = DspSharingLinksAttributes.from_json(json)
# print the JSON string representation of the object
print(DspSharingLinksAttributes.to_json())

# convert the object into a dict
dsp_sharing_links_attributes_dict = dsp_sharing_links_attributes_instance.to_dict()
# create an instance of DspSharingLinksAttributes from a dict
dsp_sharing_links_attributes_from_dict = DspSharingLinksAttributes.from_dict(dsp_sharing_links_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


