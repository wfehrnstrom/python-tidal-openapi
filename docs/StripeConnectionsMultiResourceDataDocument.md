# StripeConnectionsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StripeConnectionsResourceObject]**](StripeConnectionsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.stripe_connections_multi_resource_data_document import StripeConnectionsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsMultiResourceDataDocument from a JSON string
stripe_connections_multi_resource_data_document_instance = StripeConnectionsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsMultiResourceDataDocument.to_json())

# convert the object into a dict
stripe_connections_multi_resource_data_document_dict = stripe_connections_multi_resource_data_document_instance.to_dict()
# create an instance of StripeConnectionsMultiResourceDataDocument from a dict
stripe_connections_multi_resource_data_document_from_dict = StripeConnectionsMultiResourceDataDocument.from_dict(stripe_connections_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


