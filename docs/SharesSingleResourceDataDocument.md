# SharesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SharesResourceObject**](SharesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.shares_single_resource_data_document import SharesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SharesSingleResourceDataDocument from a JSON string
shares_single_resource_data_document_instance = SharesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SharesSingleResourceDataDocument.to_json())

# convert the object into a dict
shares_single_resource_data_document_dict = shares_single_resource_data_document_instance.to_dict()
# create an instance of SharesSingleResourceDataDocument from a dict
shares_single_resource_data_document_from_dict = SharesSingleResourceDataDocument.from_dict(shares_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


