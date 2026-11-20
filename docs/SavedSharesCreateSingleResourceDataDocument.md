# SavedSharesCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SavedSharesResourceObject**](SavedSharesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.saved_shares_create_single_resource_data_document import SavedSharesCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSharesCreateSingleResourceDataDocument from a JSON string
saved_shares_create_single_resource_data_document_instance = SavedSharesCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SavedSharesCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
saved_shares_create_single_resource_data_document_dict = saved_shares_create_single_resource_data_document_instance.to_dict()
# create an instance of SavedSharesCreateSingleResourceDataDocument from a dict
saved_shares_create_single_resource_data_document_from_dict = SavedSharesCreateSingleResourceDataDocument.from_dict(saved_shares_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


