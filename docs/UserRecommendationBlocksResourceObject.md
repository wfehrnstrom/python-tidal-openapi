# UserRecommendationBlocksResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**UserRecommendationBlocksRelationships**](UserRecommendationBlocksRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.user_recommendation_blocks_resource_object import UserRecommendationBlocksResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksResourceObject from a JSON string
user_recommendation_blocks_resource_object_instance = UserRecommendationBlocksResourceObject.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksResourceObject.to_json())

# convert the object into a dict
user_recommendation_blocks_resource_object_dict = user_recommendation_blocks_resource_object_instance.to_dict()
# create an instance of UserRecommendationBlocksResourceObject from a dict
user_recommendation_blocks_resource_object_from_dict = UserRecommendationBlocksResourceObject.from_dict(user_recommendation_blocks_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


