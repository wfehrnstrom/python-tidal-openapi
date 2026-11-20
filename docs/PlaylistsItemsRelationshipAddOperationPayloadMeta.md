# PlaylistsItemsRelationshipAddOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_duplicates** | **str** | How to handle available items already present in the playlist. Presence is evaluated against playlist state immediately before the operation; duplicate occurrences within this request do not make one another already present. ADD adds every requested occurrence. FAIL returns 409 and adds nothing when any requested resource type and id is already present. SKIP adds only absent resources and reports every omitted occurrence in response meta.skipped with reason ALREADY_PRESENT. Track and video identities with the same id are distinct. Defaults to ADD. | [optional] [default to 'ADD']
**position_before** | **str** |  | [optional] 

## Example

```python
from tidal.models.playlists_items_relationship_add_operation_payload_meta import PlaylistsItemsRelationshipAddOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsItemsRelationshipAddOperationPayloadMeta from a JSON string
playlists_items_relationship_add_operation_payload_meta_instance = PlaylistsItemsRelationshipAddOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(PlaylistsItemsRelationshipAddOperationPayloadMeta.to_json())

# convert the object into a dict
playlists_items_relationship_add_operation_payload_meta_dict = playlists_items_relationship_add_operation_payload_meta_instance.to_dict()
# create an instance of PlaylistsItemsRelationshipAddOperationPayloadMeta from a dict
playlists_items_relationship_add_operation_payload_meta_from_dict = PlaylistsItemsRelationshipAddOperationPayloadMeta.from_dict(playlists_items_relationship_add_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


