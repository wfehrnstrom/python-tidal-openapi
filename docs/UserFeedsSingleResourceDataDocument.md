# UserFeedsSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserFeedsResourceObject**](UserFeedsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_feeds_single_resource_data_document import UserFeedsSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsSingleResourceDataDocument from a JSON string
user_feeds_single_resource_data_document_instance = UserFeedsSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserFeedsSingleResourceDataDocument.to_json())

# convert the object into a dict
user_feeds_single_resource_data_document_dict = user_feeds_single_resource_data_document_instance.to_dict()
# create an instance of UserFeedsSingleResourceDataDocument from a dict
user_feeds_single_resource_data_document_from_dict = UserFeedsSingleResourceDataDocument.from_dict(user_feeds_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


