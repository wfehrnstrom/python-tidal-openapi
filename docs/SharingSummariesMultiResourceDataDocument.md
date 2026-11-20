# SharingSummariesMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SharingSummariesResourceObject]**](SharingSummariesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.sharing_summaries_multi_resource_data_document import SharingSummariesMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SharingSummariesMultiResourceDataDocument from a JSON string
sharing_summaries_multi_resource_data_document_instance = SharingSummariesMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SharingSummariesMultiResourceDataDocument.to_json())

# convert the object into a dict
sharing_summaries_multi_resource_data_document_dict = sharing_summaries_multi_resource_data_document_instance.to_dict()
# create an instance of SharingSummariesMultiResourceDataDocument from a dict
sharing_summaries_multi_resource_data_document_from_dict = SharingSummariesMultiResourceDataDocument.from_dict(sharing_summaries_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


