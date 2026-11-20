# InstallationsOfflineInventoryRelationshipAddOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstallationsOfflineInventoryItemIdentifier]**](InstallationsOfflineInventoryItemIdentifier.md) |  | 

## Example

```python
from tidal.models.installations_offline_inventory_relationship_add_operation_payload import InstallationsOfflineInventoryRelationshipAddOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsOfflineInventoryRelationshipAddOperationPayload from a JSON string
installations_offline_inventory_relationship_add_operation_payload_instance = InstallationsOfflineInventoryRelationshipAddOperationPayload.from_json(json)
# print the JSON string representation of the object
print(InstallationsOfflineInventoryRelationshipAddOperationPayload.to_json())

# convert the object into a dict
installations_offline_inventory_relationship_add_operation_payload_dict = installations_offline_inventory_relationship_add_operation_payload_instance.to_dict()
# create an instance of InstallationsOfflineInventoryRelationshipAddOperationPayload from a dict
installations_offline_inventory_relationship_add_operation_payload_from_dict = InstallationsOfflineInventoryRelationshipAddOperationPayload.from_dict(installations_offline_inventory_relationship_add_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


