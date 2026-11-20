# StripeDashboardLinksAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_link** | [**LinkObject**](LinkObject.md) |  | [optional] 

## Example

```python
from tidal.models.stripe_dashboard_links_attributes import StripeDashboardLinksAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of StripeDashboardLinksAttributes from a JSON string
stripe_dashboard_links_attributes_instance = StripeDashboardLinksAttributes.from_json(json)
# print the JSON string representation of the object
print(StripeDashboardLinksAttributes.to_json())

# convert the object into a dict
stripe_dashboard_links_attributes_dict = stripe_dashboard_links_attributes_instance.to_dict()
# create an instance of StripeDashboardLinksAttributes from a dict
stripe_dashboard_links_attributes_from_dict = StripeDashboardLinksAttributes.from_dict(stripe_dashboard_links_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


