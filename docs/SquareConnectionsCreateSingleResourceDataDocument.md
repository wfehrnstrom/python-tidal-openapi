# SquareConnectionsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareConnectionsResourceObject**](SquareConnectionsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_connections_create_single_resource_data_document import SquareConnectionsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsCreateSingleResourceDataDocument from a JSON string
square_connections_create_single_resource_data_document_instance = SquareConnectionsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
square_connections_create_single_resource_data_document_dict = square_connections_create_single_resource_data_document_instance.to_dict()
# create an instance of SquareConnectionsCreateSingleResourceDataDocument from a dict
square_connections_create_single_resource_data_document_from_dict = SquareConnectionsCreateSingleResourceDataDocument.from_dict(square_connections_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


