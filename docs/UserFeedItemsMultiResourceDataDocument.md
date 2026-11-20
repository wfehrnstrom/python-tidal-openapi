# UserFeedItemsMultiResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserFeedItemsResourceObject]**](UserFeedItemsResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 
**meta** | [**UserFeedItemsMultiResourceDataDocumentMeta**](UserFeedItemsMultiResourceDataDocumentMeta.md) |  | [optional] 

## Example

```python
from tidal.models.user_feed_items_multi_resource_data_document import UserFeedItemsMultiResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedItemsMultiResourceDataDocument from a JSON string
user_feed_items_multi_resource_data_document_instance = UserFeedItemsMultiResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserFeedItemsMultiResourceDataDocument.to_json())

# convert the object into a dict
user_feed_items_multi_resource_data_document_dict = user_feed_items_multi_resource_data_document_instance.to_dict()
# create an instance of UserFeedItemsMultiResourceDataDocument from a dict
user_feed_items_multi_resource_data_document_from_dict = UserFeedItemsMultiResourceDataDocument.from_dict(user_feed_items_multi_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


