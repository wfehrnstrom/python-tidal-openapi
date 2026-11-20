# InstallationsOfflineInventoryRelationshipRemoveOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstallationsOfflineInventoryItemIdentifier]**](InstallationsOfflineInventoryItemIdentifier.md) |  | 

## Example

```python
from tidal.models.installations_offline_inventory_relationship_remove_operation_payload import InstallationsOfflineInventoryRelationshipRemoveOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsOfflineInventoryRelationshipRemoveOperationPayload from a JSON string
installations_offline_inventory_relationship_remove_operation_payload_instance = InstallationsOfflineInventoryRelationshipRemoveOperationPayload.from_json(json)
# print the JSON string representation of the object
print(InstallationsOfflineInventoryRelationshipRemoveOperationPayload.to_json())

# convert the object into a dict
installations_offline_inventory_relationship_remove_operation_payload_dict = installations_offline_inventory_relationship_remove_operation_payload_instance.to_dict()
# create an instance of InstallationsOfflineInventoryRelationshipRemoveOperationPayload from a dict
installations_offline_inventory_relationship_remove_operation_payload_from_dict = InstallationsOfflineInventoryRelationshipRemoveOperationPayload.from_dict(installations_offline_inventory_relationship_remove_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


