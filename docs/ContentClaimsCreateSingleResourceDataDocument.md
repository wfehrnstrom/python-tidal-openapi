# ContentClaimsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ContentClaimsResourceObject**](ContentClaimsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.content_claims_create_single_resource_data_document import ContentClaimsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsCreateSingleResourceDataDocument from a JSON string
content_claims_create_single_resource_data_document_instance = ContentClaimsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
content_claims_create_single_resource_data_document_dict = content_claims_create_single_resource_data_document_instance.to_dict()
# create an instance of ContentClaimsCreateSingleResourceDataDocument from a dict
content_claims_create_single_resource_data_document_from_dict = ContentClaimsCreateSingleResourceDataDocument.from_dict(content_claims_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


