# SharesUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SharesResourceObject**](SharesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.shares_update_single_resource_data_document import SharesUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SharesUpdateSingleResourceDataDocument from a JSON string
shares_update_single_resource_data_document_instance = SharesUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SharesUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
shares_update_single_resource_data_document_dict = shares_update_single_resource_data_document_instance.to_dict()
# create an instance of SharesUpdateSingleResourceDataDocument from a dict
shares_update_single_resource_data_document_from_dict = SharesUpdateSingleResourceDataDocument.from_dict(shares_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


