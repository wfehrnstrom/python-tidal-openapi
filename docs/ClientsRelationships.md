# ClientsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**ClientsCertificatesMultiRelationshipDataDocument**](ClientsCertificatesMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**ClientsOwnersMultiRelationshipDataDocument**](ClientsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.clients_relationships import ClientsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsRelationships from a JSON string
clients_relationships_instance = ClientsRelationships.from_json(json)
# print the JSON string representation of the object
print(ClientsRelationships.to_json())

# convert the object into a dict
clients_relationships_dict = clients_relationships_instance.to_dict()
# create an instance of ClientsRelationships from a dict
clients_relationships_from_dict = ClientsRelationships.from_dict(clients_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


