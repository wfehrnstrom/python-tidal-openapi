# ClientsCertificatesMultiRelationshipDataDocument

Target resource types: `clientCertificates`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.clients_certificates_multi_relationship_data_document import ClientsCertificatesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsCertificatesMultiRelationshipDataDocument from a JSON string
clients_certificates_multi_relationship_data_document_instance = ClientsCertificatesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ClientsCertificatesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
clients_certificates_multi_relationship_data_document_dict = clients_certificates_multi_relationship_data_document_instance.to_dict()
# create an instance of ClientsCertificatesMultiRelationshipDataDocument from a dict
clients_certificates_multi_relationship_data_document_from_dict = ClientsCertificatesMultiRelationshipDataDocument.from_dict(clients_certificates_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


