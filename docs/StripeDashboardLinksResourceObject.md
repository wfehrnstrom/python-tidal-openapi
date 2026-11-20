# StripeDashboardLinksResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**StripeDashboardLinksAttributes**](StripeDashboardLinksAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**StripeDashboardLinksRelationships**](StripeDashboardLinksRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.stripe_dashboard_links_resource_object import StripeDashboardLinksResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of StripeDashboardLinksResourceObject from a JSON string
stripe_dashboard_links_resource_object_instance = StripeDashboardLinksResourceObject.from_json(json)
# print the JSON string representation of the object
print(StripeDashboardLinksResourceObject.to_json())

# convert the object into a dict
stripe_dashboard_links_resource_object_dict = stripe_dashboard_links_resource_object_instance.to_dict()
# create an instance of StripeDashboardLinksResourceObject from a dict
stripe_dashboard_links_resource_object_from_dict = StripeDashboardLinksResourceObject.from_dict(stripe_dashboard_links_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


