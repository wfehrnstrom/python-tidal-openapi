# DynamicModulesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_actions** | **List[str]** | Actions available in the module header. SPOTLIGHT_INFO opens information about TIDAL Spotlight. Clients choose the presentation and ignore unsupported actions, including UNKNOWN. | 
**preview_layout** | **str** | Presentation family for items in a dynamic module preview. The API selects the semantic presentation intent while clients own platform-specific geometry. A layout does not prescribe scroll direction, row or column count, dimensions, spacing, breakpoints, or visible item count; clients preserve the server-provided item order. GRID means artwork-forward tiles or cards. LIST means detail-forward row cells, which clients may arrange in one or more columns. SHORTCUT means compact quick-access items, which clients may arrange as a responsive grid or rail. UNKNOWN is the forward-compatible default; clients should skip the module or use a safe default. | 
**subtitle** | **str** | Subtitle of the module | [optional] 
**title** | **str** | Title of the module | [optional] 
**view_all_layout** | **str** | Presentation family for items on a dynamic module&#39;s view-all screen. The API selects the semantic presentation intent while clients own platform-specific geometry. A layout does not prescribe scroll direction, row or column count, dimensions, spacing, or breakpoints; clients preserve the server-provided item order. When viewAllLayout is omitted, the module has no view-all screen. GRID means artwork-forward tiles or cards. LIST means detail-forward row cells, which clients may arrange in one or more columns or as a table. UNKNOWN is the forward-compatible default; clients should skip the module or use a safe default. | [optional] 

## Example

```python
from tidal.models.dynamic_modules_attributes import DynamicModulesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicModulesAttributes from a JSON string
dynamic_modules_attributes_instance = DynamicModulesAttributes.from_json(json)
# print the JSON string representation of the object
print(DynamicModulesAttributes.to_json())

# convert the object into a dict
dynamic_modules_attributes_dict = dynamic_modules_attributes_instance.to_dict()
# create an instance of DynamicModulesAttributes from a dict
dynamic_modules_attributes_from_dict = DynamicModulesAttributes.from_dict(dynamic_modules_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


