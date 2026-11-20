# StripeConnectionsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.stripe_connections_owners_multi_relationship_data_document import StripeConnectionsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsOwnersMultiRelationshipDataDocument from a JSON string
stripe_connections_owners_multi_relationship_data_document_instance = StripeConnectionsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
stripe_connections_owners_multi_relationship_data_document_dict = stripe_connections_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of StripeConnectionsOwnersMultiRelationshipDataDocument from a dict
stripe_connections_owners_multi_relationship_data_document_from_dict = StripeConnectionsOwnersMultiRelationshipDataDocument.from_dict(stripe_connections_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


