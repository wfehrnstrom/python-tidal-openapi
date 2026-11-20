# UserFeedsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed** | [**UserFeedsUpdateOperationPayloadDataAttributesFeed**](UserFeedsUpdateOperationPayloadDataAttributesFeed.md) |  | [optional] 
**inbox** | [**UserFeedsUpdateOperationPayloadDataAttributesInbox**](UserFeedsUpdateOperationPayloadDataAttributesInbox.md) |  | [optional] 

## Example

```python
from tidal.models.user_feeds_update_operation_payload_data_attributes import UserFeedsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsUpdateOperationPayloadDataAttributes from a JSON string
user_feeds_update_operation_payload_data_attributes_instance = UserFeedsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(UserFeedsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
user_feeds_update_operation_payload_data_attributes_dict = user_feeds_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of UserFeedsUpdateOperationPayloadDataAttributes from a dict
user_feeds_update_operation_payload_data_attributes_from_dict = UserFeedsUpdateOperationPayloadDataAttributes.from_dict(user_feeds_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


