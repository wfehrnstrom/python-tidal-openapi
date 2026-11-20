# SquareConnectionsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SquareConnectionsResourceObject**](SquareConnectionsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.square_connections_single_resource_data_document import SquareConnectionsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsSingleResourceDataDocument from a JSON string
square_connections_single_resource_data_document_instance = SquareConnectionsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsSingleResourceDataDocument.to_json())

# convert the object into a dict
square_connections_single_resource_data_document_dict = square_connections_single_resource_data_document_instance.to_dict()
# create an instance of SquareConnectionsSingleResourceDataDocument from a dict
square_connections_single_resource_data_document_from_dict = SquareConnectionsSingleResourceDataDocument.from_dict(square_connections_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


