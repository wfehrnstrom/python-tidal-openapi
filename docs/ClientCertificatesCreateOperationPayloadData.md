# ClientCertificatesCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | [**ClientCertificatesCreateOperationPayloadDataRelationships**](ClientCertificatesCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.client_certificates_create_operation_payload_data import ClientCertificatesCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificatesCreateOperationPayloadData from a JSON string
client_certificates_create_operation_payload_data_instance = ClientCertificatesCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ClientCertificatesCreateOperationPayloadData.to_json())

# convert the object into a dict
client_certificates_create_operation_payload_data_dict = client_certificates_create_operation_payload_data_instance.to_dict()
# create an instance of ClientCertificatesCreateOperationPayloadData from a dict
client_certificates_create_operation_payload_data_from_dict = ClientCertificatesCreateOperationPayloadData.from_dict(client_certificates_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


