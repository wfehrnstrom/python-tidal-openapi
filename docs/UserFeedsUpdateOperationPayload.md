# UserFeedsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserFeedsUpdateOperationPayloadData**](UserFeedsUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.user_feeds_update_operation_payload import UserFeedsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsUpdateOperationPayload from a JSON string
user_feeds_update_operation_payload_instance = UserFeedsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(UserFeedsUpdateOperationPayload.to_json())

# convert the object into a dict
user_feeds_update_operation_payload_dict = user_feeds_update_operation_payload_instance.to_dict()
# create an instance of UserFeedsUpdateOperationPayload from a dict
user_feeds_update_operation_payload_from_dict = UserFeedsUpdateOperationPayload.from_dict(user_feeds_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


