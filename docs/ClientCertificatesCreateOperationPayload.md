# ClientCertificatesCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientCertificatesCreateOperationPayloadData**](ClientCertificatesCreateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.client_certificates_create_operation_payload import ClientCertificatesCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificatesCreateOperationPayload from a JSON string
client_certificates_create_operation_payload_instance = ClientCertificatesCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ClientCertificatesCreateOperationPayload.to_json())

# convert the object into a dict
client_certificates_create_operation_payload_dict = client_certificates_create_operation_payload_instance.to_dict()
# create an instance of ClientCertificatesCreateOperationPayload from a dict
client_certificates_create_operation_payload_from_dict = ClientCertificatesCreateOperationPayload.from_dict(client_certificates_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


