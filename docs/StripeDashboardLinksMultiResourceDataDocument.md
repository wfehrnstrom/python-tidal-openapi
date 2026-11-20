# StripeDashboardLinksMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StripeDashboardLinksResourceObject]**](StripeDashboardLinksResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.stripe_dashboard_links_multi_resource_data_document import StripeDashboardLinksMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StripeDashboardLinksMultiResourceDataDocument from a JSON string
stripe_dashboard_links_multi_resource_data_document_instance = StripeDashboardLinksMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(StripeDashboardLinksMultiResourceDataDocument.to_json())

# convert the object into a dict
stripe_dashboard_links_multi_resource_data_document_dict = stripe_dashboard_links_multi_resource_data_document_instance.to_dict()
# create an instance of StripeDashboardLinksMultiResourceDataDocument from a dict
stripe_dashboard_links_multi_resource_data_document_from_dict = StripeDashboardLinksMultiResourceDataDocument.from_dict(stripe_dashboard_links_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


