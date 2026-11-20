# UserCollectionArtistsItemsRelationshipAddOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**meta** | [**UserCollectionArtistsItemsRelationshipAddOperationPayloadDataMeta**](UserCollectionArtistsItemsRelationshipAddOperationPayloadDataMeta.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from tidal.models.user_collection_artists_items_relationship_add_operation_payload_data import UserCollectionArtistsItemsRelationshipAddOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionArtistsItemsRelationshipAddOperationPayloadData from a JSON string
user_collection_artists_items_relationship_add_operation_payload_data_instance = UserCollectionArtistsItemsRelationshipAddOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(UserCollectionArtistsItemsRelationshipAddOperationPayloadData.to_json())

# convert the object into a dict
user_collection_artists_items_relationship_add_operation_payload_data_dict = user_collection_artists_items_relationship_add_operation_payload_data_instance.to_dict()
# create an instance of UserCollectionArtistsItemsRelationshipAddOperationPayloadData from a dict
user_collection_artists_items_relationship_add_operation_payload_data_from_dict = UserCollectionArtistsItemsRelationshipAddOperationPayloadData.from_dict(user_collection_artists_items_relationship_add_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


