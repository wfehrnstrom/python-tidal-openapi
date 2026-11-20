# UserFeedsUpdateSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserFeedsResourceObject**](UserFeedsResourceObject.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_feeds_update_single_resource_data_document import UserFeedsUpdateSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedsUpdateSingleResourceDataDocument from a JSON string
user_feeds_update_single_resource_data_document_instance = UserFeedsUpdateSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserFeedsUpdateSingleResourceDataDocument.to_json())

# convert the object into a dict
user_feeds_update_single_resource_data_document_dict = user_feeds_update_single_resource_data_document_instance.to_dict()
# create an instance of UserFeedsUpdateSingleResourceDataDocument from a dict
user_feeds_update_single_resource_data_document_from_dict = UserFeedsUpdateSingleResourceDataDocument.from_dict(user_feeds_update_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


