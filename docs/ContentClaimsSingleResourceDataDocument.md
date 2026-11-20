# ContentClaimsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ContentClaimsResourceObject**](ContentClaimsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.content_claims_single_resource_data_document import ContentClaimsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsSingleResourceDataDocument from a JSON string
content_claims_single_resource_data_document_instance = ContentClaimsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsSingleResourceDataDocument.to_json())

# convert the object into a dict
content_claims_single_resource_data_document_dict = content_claims_single_resource_data_document_instance.to_dict()
# create an instance of ContentClaimsSingleResourceDataDocument from a dict
content_claims_single_resource_data_document_from_dict = ContentClaimsSingleResourceDataDocument.from_dict(content_claims_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


