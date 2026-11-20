# ClientCertificatesCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientCertificatesResourceObject**](ClientCertificatesResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.client_certificates_create_single_resource_data_document import ClientCertificatesCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificatesCreateSingleResourceDataDocument from a JSON string
client_certificates_create_single_resource_data_document_instance = ClientCertificatesCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ClientCertificatesCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
client_certificates_create_single_resource_data_document_dict = client_certificates_create_single_resource_data_document_instance.to_dict()
# create an instance of ClientCertificatesCreateSingleResourceDataDocument from a dict
client_certificates_create_single_resource_data_document_from_dict = ClientCertificatesCreateSingleResourceDataDocument.from_dict(client_certificates_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


