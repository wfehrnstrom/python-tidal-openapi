# ErrorsDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorObject]**](ErrorObject.md) | Array of error objects | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

## Example

```python
from tidal.models.errors_document import ErrorsDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsDocument from a JSON string
errors_document_instance = ErrorsDocument.from_json(json)
# print the JSON string representation of the object
print(ErrorsDocument.to_json())

# convert the object into a dict
errors_document_dict = errors_document_instance.to_dict()
# create an instance of ErrorsDocument from a dict
errors_document_from_dict = ErrorsDocument.from_dict(errors_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


