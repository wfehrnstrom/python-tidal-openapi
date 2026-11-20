# ArtistsFollowingRelationshipAddOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsFollowingRelationshipAddOperationPayloadData]**](ArtistsFollowingRelationshipAddOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.artists_following_relationship_add_operation_payload import ArtistsFollowingRelationshipAddOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsFollowingRelationshipAddOperationPayload from a JSON string
artists_following_relationship_add_operation_payload_instance = ArtistsFollowingRelationshipAddOperationPayload.from_json(json)
# print the JSON string representation of the object
print(ArtistsFollowingRelationshipAddOperationPayload.to_json())

# convert the object into a dict
artists_following_relationship_add_operation_payload_dict = artists_following_relationship_add_operation_payload_instance.to_dict()
# create an instance of ArtistsFollowingRelationshipAddOperationPayload from a dict
artists_following_relationship_add_operation_payload_from_dict = ArtistsFollowingRelationshipAddOperationPayload.from_dict(artists_following_relationship_add_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


