# ContentClaimsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ContentClaimsResourceObject]**](ContentClaimsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.content_claims_multi_resource_data_document import ContentClaimsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsMultiResourceDataDocument from a JSON string
content_claims_multi_resource_data_document_instance = ContentClaimsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsMultiResourceDataDocument.to_json())

# convert the object into a dict
content_claims_multi_resource_data_document_dict = content_claims_multi_resource_data_document_instance.to_dict()
# create an instance of ContentClaimsMultiResourceDataDocument from a dict
content_claims_multi_resource_data_document_from_dict = ContentClaimsMultiResourceDataDocument.from_dict(content_claims_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


