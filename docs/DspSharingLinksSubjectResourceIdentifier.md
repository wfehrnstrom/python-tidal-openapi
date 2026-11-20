# DspSharingLinksSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**DspSharingLinksSubjectResourceIdentifierMeta**](DspSharingLinksSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.dsp_sharing_links_subject_resource_identifier import DspSharingLinksSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of DspSharingLinksSubjectResourceIdentifier from a JSON string
dsp_sharing_links_subject_resource_identifier_instance = DspSharingLinksSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(DspSharingLinksSubjectResourceIdentifier.to_json())

# convert the object into a dict
dsp_sharing_links_subject_resource_identifier_dict = dsp_sharing_links_subject_resource_identifier_instance.to_dict()
# create an instance of DspSharingLinksSubjectResourceIdentifier from a dict
dsp_sharing_links_subject_resource_identifier_from_dict = DspSharingLinksSubjectResourceIdentifier.from_dict(dsp_sharing_links_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


