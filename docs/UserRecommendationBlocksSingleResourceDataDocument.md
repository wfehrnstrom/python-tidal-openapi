# UserRecommendationBlocksSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserRecommendationBlocksResourceObject**](UserRecommendationBlocksResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_recommendation_blocks_single_resource_data_document import UserRecommendationBlocksSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecommendationBlocksSingleResourceDataDocument from a JSON string
user_recommendation_blocks_single_resource_data_document_instance = UserRecommendationBlocksSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserRecommendationBlocksSingleResourceDataDocument.to_json())

# convert the object into a dict
user_recommendation_blocks_single_resource_data_document_dict = user_recommendation_blocks_single_resource_data_document_instance.to_dict()
# create an instance of UserRecommendationBlocksSingleResourceDataDocument from a dict
user_recommendation_blocks_single_resource_data_document_from_dict = UserRecommendationBlocksSingleResourceDataDocument.from_dict(user_recommendation_blocks_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


