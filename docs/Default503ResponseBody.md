# Default503ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations503ResponseBodyErrorsInner]**](AtomicOperations503ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.default503_response_body import Default503ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Default503ResponseBody from a JSON string
default503_response_body_instance = Default503ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Default503ResponseBody.to_json())

# convert the object into a dict
default503_response_body_dict = default503_response_body_instance.to_dict()
# create an instance of Default503ResponseBody from a dict
default503_response_body_from_dict = Default503ResponseBody.from_dict(default503_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


