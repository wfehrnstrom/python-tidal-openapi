# StripeDashboardLinksOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.stripe_dashboard_links_owners_multi_relationship_data_document import StripeDashboardLinksOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StripeDashboardLinksOwnersMultiRelationshipDataDocument from a JSON string
stripe_dashboard_links_owners_multi_relationship_data_document_instance = StripeDashboardLinksOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(StripeDashboardLinksOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
stripe_dashboard_links_owners_multi_relationship_data_document_dict = stripe_dashboard_links_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of StripeDashboardLinksOwnersMultiRelationshipDataDocument from a dict
stripe_dashboard_links_owners_multi_relationship_data_document_from_dict = StripeDashboardLinksOwnersMultiRelationshipDataDocument.from_dict(stripe_dashboard_links_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


