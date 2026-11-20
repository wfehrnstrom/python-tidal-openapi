# ReactionsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReactionsResourceObject**](ReactionsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.reactions_create_single_resource_data_document import ReactionsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsCreateSingleResourceDataDocument from a JSON string
reactions_create_single_resource_data_document_instance = ReactionsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ReactionsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
reactions_create_single_resource_data_document_dict = reactions_create_single_resource_data_document_instance.to_dict()
# create an instance of ReactionsCreateSingleResourceDataDocument from a dict
reactions_create_single_resource_data_document_from_dict = ReactionsCreateSingleResourceDataDocument.from_dict(reactions_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


