# DspSharingLinksSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `artists`, `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DspSharingLinksSubjectResourceIdentifier**](DspSharingLinksSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dsp_sharing_links_subject_single_relationship_data_document import DspSharingLinksSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DspSharingLinksSubjectSingleRelationshipDataDocument from a JSON string
dsp_sharing_links_subject_single_relationship_data_document_instance = DspSharingLinksSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(DspSharingLinksSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
dsp_sharing_links_subject_single_relationship_data_document_dict = dsp_sharing_links_subject_single_relationship_data_document_instance.to_dict()
# create an instance of DspSharingLinksSubjectSingleRelationshipDataDocument from a dict
dsp_sharing_links_subject_single_relationship_data_document_from_dict = DspSharingLinksSubjectSingleRelationshipDataDocument.from_dict(dsp_sharing_links_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


