# ClientCertificatesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientCertificatesResourceObject**](ClientCertificatesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.client_certificates_single_resource_data_document import ClientCertificatesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificatesSingleResourceDataDocument from a JSON string
client_certificates_single_resource_data_document_instance = ClientCertificatesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(ClientCertificatesSingleResourceDataDocument.to_json())

# convert the object into a dict
client_certificates_single_resource_data_document_dict = client_certificates_single_resource_data_document_instance.to_dict()
# create an instance of ClientCertificatesSingleResourceDataDocument from a dict
client_certificates_single_resource_data_document_from_dict = ClientCertificatesSingleResourceDataDocument.from_dict(client_certificates_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


