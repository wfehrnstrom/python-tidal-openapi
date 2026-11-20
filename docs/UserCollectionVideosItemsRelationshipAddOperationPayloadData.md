# UserCollectionVideosItemsRelationshipAddOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**UserCollectionVideosItemsRelationshipAddOperationPayloadDataMeta**](UserCollectionVideosItemsRelationshipAddOperationPayloadDataMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_collection_videos_items_relationship_add_operation_payload_data import UserCollectionVideosItemsRelationshipAddOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionVideosItemsRelationshipAddOperationPayloadData from a JSON string
user_collection_videos_items_relationship_add_operation_payload_data_instance = UserCollectionVideosItemsRelationshipAddOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserCollectionVideosItemsRelationshipAddOperationPayloadData.to_json())

# convert the object into a dict
user_collection_videos_items_relationship_add_operation_payload_data_dict = user_collection_videos_items_relationship_add_operation_payload_data_instance.to_dict()
# create an instance of UserCollectionVideosItemsRelationshipAddOperationPayloadData from a dict
user_collection_videos_items_relationship_add_operation_payload_data_from_dict = UserCollectionVideosItemsRelationshipAddOperationPayloadData.from_dict(user_collection_videos_items_relationship_add_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


