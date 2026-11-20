# Idempotency409ResponseBodyErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**detail** | **str** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from tidal.models.idempotency409_response_body_errors_inner import Idempotency409ResponseBodyErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Idempotency409ResponseBodyErrorsInner from a JSON string
idempotency409_response_body_errors_inner_instance = Idempotency409ResponseBodyErrorsInner.from_json(json)
# print the JSON string representation of the object
print(Idempotency409ResponseBodyErrorsInner.to_json())

# convert the object into a dict
idempotency409_response_body_errors_inner_dict = idempotency409_response_body_errors_inner_instance.to_dict()
# create an instance of Idempotency409ResponseBodyErrorsInner from a dict
idempotency409_response_body_errors_inner_from_dict = Idempotency409ResponseBodyErrorsInner.from_dict(idempotency409_response_body_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


