# Idempotency422ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[AtomicOperations422ResponseBodyErrorsInner]**](AtomicOperations422ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Idempotency422ResponseBody from a JSON string
idempotency422_response_body_instance = Idempotency422ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Idempotency422ResponseBody.to_json())

# convert the object into a dict
idempotency422_response_body_dict = idempotency422_response_body_instance.to_dict()
# create an instance of Idempotency422ResponseBody from a dict
idempotency422_response_body_from_dict = Idempotency422ResponseBody.from_dict(idempotency422_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


