# PlayQueuesFutureResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **UUID** |  | 
**item_id** | **str** |  | 
**legacy_source** | [**LegacySource**](LegacySource.md) |  | [optional] 
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.play_queues_future_resource_identifier_meta import PlayQueuesFutureResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueuesFutureResourceIdentifierMeta from a JSON string
play_queues_future_resource_identifier_meta_instance = PlayQueuesFutureResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(PlayQueuesFutureResourceIdentifierMeta.to_json())

# convert the object into a dict
play_queues_future_resource_identifier_meta_dict = play_queues_future_resource_identifier_meta_instance.to_dict()
# create an instance of PlayQueuesFutureResourceIdentifierMeta from a dict
play_queues_future_resource_identifier_meta_from_dict = PlayQueuesFutureResourceIdentifierMeta.from_dict(play_queues_future_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


