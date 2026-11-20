# ClientCertificatesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**ClientCertificatesOwnersMultiRelationshipDataDocument**](ClientCertificatesOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.client_certificates_relationships import ClientCertificatesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificatesRelationships from a JSON string
client_certificates_relationships_instance = ClientCertificatesRelationships.from_json(json)
# print the JSON string representation of the object
print(ClientCertificatesRelationships.to_json())

# convert the object into a dict
client_certificates_relationships_dict = client_certificates_relationships_instance.to_dict()
# create an instance of ClientCertificatesRelationships from a dict
client_certificates_relationships_from_dict = ClientCertificatesRelationships.from_dict(client_certificates_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


