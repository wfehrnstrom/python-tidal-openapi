# AcceptedTermsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AcceptedTermsCreateOperationPayloadData**](AcceptedTermsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.accepted_terms_create_operation_payload import AcceptedTermsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedTermsCreateOperationPayload from a JSON string
accepted_terms_create_operation_payload_instance = AcceptedTermsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(AcceptedTermsCreateOperationPayload.to_json())

# convert the object into a dict
accepted_terms_create_operation_payload_dict = accepted_terms_create_operation_payload_instance.to_dict()
# create an instance of AcceptedTermsCreateOperationPayload from a dict
accepted_terms_create_operation_payload_from_dict = AcceptedTermsCreateOperationPayload.from_dict(accepted_terms_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


