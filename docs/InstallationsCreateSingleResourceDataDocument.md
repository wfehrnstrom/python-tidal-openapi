# InstallationsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InstallationsResourceObject**](InstallationsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.installations_create_single_resource_data_document import InstallationsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsCreateSingleResourceDataDocument from a JSON string
installations_create_single_resource_data_document_instance = InstallationsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(InstallationsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
installations_create_single_resource_data_document_dict = installations_create_single_resource_data_document_instance.to_dict()
# create an instance of InstallationsCreateSingleResourceDataDocument from a dict
installations_create_single_resource_data_document_from_dict = InstallationsCreateSingleResourceDataDocument.from_dict(installations_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


