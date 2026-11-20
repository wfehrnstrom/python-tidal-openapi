# ClientCertificatesOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.client_certificates_owners_multi_relationship_data_document import ClientCertificatesOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificatesOwnersMultiRelationshipDataDocument from a JSON string
client_certificates_owners_multi_relationship_data_document_instance = ClientCertificatesOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ClientCertificatesOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
client_certificates_owners_multi_relationship_data_document_dict = client_certificates_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of ClientCertificatesOwnersMultiRelationshipDataDocument from a dict
client_certificates_owners_multi_relationship_data_document_from_dict = ClientCertificatesOwnersMultiRelationshipDataDocument.from_dict(client_certificates_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


