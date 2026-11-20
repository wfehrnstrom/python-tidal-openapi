# StudioHomeMerchTilesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_terms** | **List[str]** | Terms types the seller must accept before managing merch; empty when none are missing. | 

## Example

```python
from tidal.models.studio_home_merch_tiles_attributes import StudioHomeMerchTilesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeMerchTilesAttributes from a JSON string
studio_home_merch_tiles_attributes_instance = StudioHomeMerchTilesAttributes.from_json(json)
# print the JSON string representation of the object
print(StudioHomeMerchTilesAttributes.to_json())

# convert the object into a dict
studio_home_merch_tiles_attributes_dict = studio_home_merch_tiles_attributes_instance.to_dict()
# create an instance of StudioHomeMerchTilesAttributes from a dict
studio_home_merch_tiles_attributes_from_dict = StudioHomeMerchTilesAttributes.from_dict(studio_home_merch_tiles_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


