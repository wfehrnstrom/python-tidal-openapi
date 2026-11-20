# AppreciationsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AppreciationsResourceObject**](AppreciationsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.appreciations_create_single_resource_data_document import AppreciationsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AppreciationsCreateSingleResourceDataDocument from a JSON string
appreciations_create_single_resource_data_document_instance = AppreciationsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(AppreciationsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
appreciations_create_single_resource_data_document_dict = appreciations_create_single_resource_data_document_instance.to_dict()
# create an instance of AppreciationsCreateSingleResourceDataDocument from a dict
appreciations_create_single_resource_data_document_from_dict = AppreciationsCreateSingleResourceDataDocument.from_dict(appreciations_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


