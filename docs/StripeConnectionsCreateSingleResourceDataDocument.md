# StripeConnectionsCreateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StripeConnectionsResourceObject**](StripeConnectionsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.stripe_connections_create_single_resource_data_document import StripeConnectionsCreateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectionsCreateSingleResourceDataDocument from a JSON string
stripe_connections_create_single_resource_data_document_instance = StripeConnectionsCreateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(StripeConnectionsCreateSingleResourceDataDocument.to_json())

# convert the object into a dict
stripe_connections_create_single_resource_data_document_dict = stripe_connections_create_single_resource_data_document_instance.to_dict()
# create an instance of StripeConnectionsCreateSingleResourceDataDocument from a dict
stripe_connections_create_single_resource_data_document_from_dict = StripeConnectionsCreateSingleResourceDataDocument.from_dict(stripe_connections_create_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


