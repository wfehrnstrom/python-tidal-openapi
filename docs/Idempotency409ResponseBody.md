# Idempotency409ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Idempotency409ResponseBodyErrorsInner]**](Idempotency409ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of Idempotency409ResponseBody from a JSON string
idempotency409_response_body_instance = Idempotency409ResponseBody.from_json(json)
# print the JSON string representation of the object
print(Idempotency409ResponseBody.to_json())

# convert the object into a dict
idempotency409_response_body_dict = idempotency409_response_body_instance.to_dict()
# create an instance of Idempotency409ResponseBody from a dict
idempotency409_response_body_from_dict = Idempotency409ResponseBody.from_dict(idempotency409_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


