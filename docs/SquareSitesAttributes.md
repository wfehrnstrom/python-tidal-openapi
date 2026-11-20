# SquareSitesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The site&#39;s domain, if one is configured | [optional] 
**published** | **bool** | Whether the site is published on Square Online | [optional] 
**site_title** | **str** | The site&#39;s title as set by the seller in Square | [optional] 

## Example

```python
from tidal.models.square_sites_attributes import SquareSitesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareSitesAttributes from a JSON string
square_sites_attributes_instance = SquareSitesAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareSitesAttributes.to_json())

# convert the object into a dict
square_sites_attributes_dict = square_sites_attributes_instance.to_dict()
# create an instance of SquareSitesAttributes from a dict
square_sites_attributes_from_dict = SquareSitesAttributes.from_dict(square_sites_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


