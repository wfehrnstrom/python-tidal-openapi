# ErrorObjectSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** | string indicating the name of a single request header which caused the error | [optional] 
**parameter** | **str** | string indicating which URI query parameter caused the error. | [optional] 
**pointer** | **str** | a JSON Pointer [RFC6901] to the value in the request document that caused the error | [optional] 

## Example

```python
from tidal.models.error_object_source import ErrorObjectSource

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorObjectSource from a JSON string
error_object_source_instance = ErrorObjectSource.from_json(json)
# print the JSON string representation of the object
print(ErrorObjectSource.to_json())

# convert the object into a dict
error_object_source_dict = error_object_source_instance.to_dict()
# create an instance of ErrorObjectSource from a dict
error_object_source_from_dict = ErrorObjectSource.from_dict(error_object_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


