# StripeDashboardLinksRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**StripeDashboardLinksOwnersMultiRelationshipDataDocument**](StripeDashboardLinksOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.stripe_dashboard_links_relationships import StripeDashboardLinksRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of StripeDashboardLinksRelationships from a JSON string
stripe_dashboard_links_relationships_instance = StripeDashboardLinksRelationships.from_json(json)
# print the JSON string representation of the object
print(StripeDashboardLinksRelationships.to_json())

# convert the object into a dict
stripe_dashboard_links_relationships_dict = stripe_dashboard_links_relationships_instance.to_dict()
# create an instance of StripeDashboardLinksRelationships from a dict
stripe_dashboard_links_relationships_from_dict = StripeDashboardLinksRelationships.from_dict(stripe_dashboard_links_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


