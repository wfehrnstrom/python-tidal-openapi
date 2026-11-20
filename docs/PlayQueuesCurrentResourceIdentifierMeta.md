# PlayQueuesCurrentResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **UUID** |  | 
**item_id** | **str** |  | 
**legacy_source** | [**LegacySource**](LegacySource.md) |  | [optional] 
**position** | **str** |  | [optional] 
**position_revision** | **int** | Position revision for this itemId; advances only on explicit position writes. | [optional] 
**position_updated_at** | **datetime** |  | [optional] 
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 
**updated_by_installation_id** | **str** |  | [optional] 

## Example

```python
from tidal.models.play_queues_current_resource_identifier_meta import PlayQueuesCurrentResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesCurrentResourceIdentifierMeta from a JSON string
play_queues_current_resource_identifier_meta_instance = PlayQueuesCurrentResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesCurrentResourceIdentifierMeta.to_json())

# convert the object into a dict
play_queues_current_resource_identifier_meta_dict = play_queues_current_resource_identifier_meta_instance.to_dict()
# create an instance of PlayQueuesCurrentResourceIdentifierMeta from a dict
play_queues_current_resource_identifier_meta_from_dict = PlayQueuesCurrentResourceIdentifierMeta.from_dict(play_queues_current_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


