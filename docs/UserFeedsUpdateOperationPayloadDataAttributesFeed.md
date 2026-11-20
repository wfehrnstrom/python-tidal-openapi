# UserFeedsUpdateOperationPayloadDataAttributesFeed

Feed seen state

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seen_through_token** | **str** | The seen position returned in &#x60;userFeedItems.meta.seenThroughToken&#x60; for this surface. | 

## Example

```python
from tidal.models.user_feeds_update_operation_payload_data_attributes_feed import UserFeedsUpdateOperationPayloadDataAttributesFeed

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsUpdateOperationPayloadDataAttributesFeed from a JSON string
user_feeds_update_operation_payload_data_attributes_feed_instance = UserFeedsUpdateOperationPayloadDataAttributesFeed.from_json(json)
# print the JSON string representation of the object
print(UserFeedsUpdateOperationPayloadDataAttributesFeed.to_json())

# convert the object into a dict
user_feeds_update_operation_payload_data_attributes_feed_dict = user_feeds_update_operation_payload_data_attributes_feed_instance.to_dict()
# create an instance of UserFeedsUpdateOperationPayloadDataAttributesFeed from a dict
user_feeds_update_operation_payload_data_attributes_feed_from_dict = UserFeedsUpdateOperationPayloadDataAttributesFeed.from_dict(user_feeds_update_operation_payload_data_attributes_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


