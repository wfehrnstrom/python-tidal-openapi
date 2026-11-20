# SharesCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SharesResourceObject**](SharesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.shares_create_single_resource_data_document import SharesCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SharesCreateSingleResourceDataDocument from a JSON string
shares_create_single_resource_data_document_instance = SharesCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SharesCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
shares_create_single_resource_data_document_dict = shares_create_single_resource_data_document_instance.to_dict()
# create an instance of SharesCreateSingleResourceDataDocument from a dict
shares_create_single_resource_data_document_from_dict = SharesCreateSingleResourceDataDocument.from_dict(shares_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


