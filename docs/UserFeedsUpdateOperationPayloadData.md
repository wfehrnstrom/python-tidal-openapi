# UserFeedsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**UserFeedsUpdateOperationPayloadDataAttributes**](UserFeedsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** | Also accepts &#x60;me&#x60;. | 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_feeds_update_operation_payload_data import UserFeedsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsUpdateOperationPayloadData from a JSON string
user_feeds_update_operation_payload_data_instance = UserFeedsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserFeedsUpdateOperationPayloadData.to_json())

# convert the object into a dict
user_feeds_update_operation_payload_data_dict = user_feeds_update_operation_payload_data_instance.to_dict()
# create an instance of UserFeedsUpdateOperationPayloadData from a dict
user_feeds_update_operation_payload_data_from_dict = UserFeedsUpdateOperationPayloadData.from_dict(user_feeds_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


