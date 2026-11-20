# TemporaryUserTokensSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TemporaryUserTokensResourceObject**](TemporaryUserTokensResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.temporary_user_tokens_single_resource_data_document import TemporaryUserTokensSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryUserTokensSingleResourceDataDocument from a JSON string
temporary_user_tokens_single_resource_data_document_instance = TemporaryUserTokensSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(TemporaryUserTokensSingleResourceDataDocument.to_json())

# convert the object into a dict
temporary_user_tokens_single_resource_data_document_dict = temporary_user_tokens_single_resource_data_document_instance.to_dict()
# create an instance of TemporaryUserTokensSingleResourceDataDocument from a dict
temporary_user_tokens_single_resource_data_document_from_dict = TemporaryUserTokensSingleResourceDataDocument.from_dict(temporary_user_tokens_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


