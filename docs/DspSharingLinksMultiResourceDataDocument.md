# DspSharingLinksMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DspSharingLinksResourceObject]**](DspSharingLinksResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dsp_sharing_links_multi_resource_data_document import DspSharingLinksMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DspSharingLinksMultiResourceDataDocument from a JSON string
dsp_sharing_links_multi_resource_data_document_instance = DspSharingLinksMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(DspSharingLinksMultiResourceDataDocument.to_json())

# convert the object into a dict
dsp_sharing_links_multi_resource_data_document_dict = dsp_sharing_links_multi_resource_data_document_instance.to_dict()
# create an instance of DspSharingLinksMultiResourceDataDocument from a dict
dsp_sharing_links_multi_resource_data_document_from_dict = DspSharingLinksMultiResourceDataDocument.from_dict(dsp_sharing_links_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


