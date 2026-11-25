# StudioHomeMerchTilesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**StudioHomeMerchTilesItemsMultiRelationshipDataDocument**](StudioHomeMerchTilesItemsMultiRelationshipDataDocument.md) |  | [optional] 
**square_connection** | [**StudioHomeMerchTilesSquareConnectionSingleRelationshipDataDocument**](StudioHomeMerchTilesSquareConnectionSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.studio_home_merch_tiles_relationships import StudioHomeMerchTilesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of StudioHomeMerchTilesRelationships from a JSON string
studio_home_merch_tiles_relationships_instance = StudioHomeMerchTilesRelationships.from_json(json)
# print the JSON string representation of the object
print(StudioHomeMerchTilesRelationships.to_json())

# convert the object into a dict
studio_home_merch_tiles_relationships_dict = studio_home_merch_tiles_relationships_instance.to_dict()
# create an instance of StudioHomeMerchTilesRelationships from a dict
studio_home_merch_tiles_relationships_from_dict = StudioHomeMerchTilesRelationships.from_dict(studio_home_merch_tiles_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


