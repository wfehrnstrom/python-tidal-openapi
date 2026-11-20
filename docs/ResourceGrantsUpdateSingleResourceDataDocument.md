# ResourceGrantsUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceGrantsResourceObject**](ResourceGrantsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.resource_grants_update_single_resource_data_document import ResourceGrantsUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsUpdateSingleResourceDataDocument from a JSON string
resource_grants_update_single_resource_data_document_instance = ResourceGrantsUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
resource_grants_update_single_resource_data_document_dict = resource_grants_update_single_resource_data_document_instance.to_dict()
# create an instance of ResourceGrantsUpdateSingleResourceDataDocument from a dict
resource_grants_update_single_resource_data_document_from_dict = ResourceGrantsUpdateSingleResourceDataDocument.from_dict(resource_grants_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


