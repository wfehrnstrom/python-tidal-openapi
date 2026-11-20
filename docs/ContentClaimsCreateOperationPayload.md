# ContentClaimsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ContentClaimsCreateOperationPayloadData**](ContentClaimsCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.content_claims_create_operation_payload import ContentClaimsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsCreateOperationPayload from a JSON string
content_claims_create_operation_payload_instance = ContentClaimsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsCreateOperationPayload.to_json())

# convert the object into a dict
content_claims_create_operation_payload_dict = content_claims_create_operation_payload_instance.to_dict()
# create an instance of ContentClaimsCreateOperationPayload from a dict
content_claims_create_operation_payload_from_dict = ContentClaimsCreateOperationPayload.from_dict(content_claims_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


