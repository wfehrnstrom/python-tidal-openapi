# InstallationsOfflineInventoryResourceIdentifierMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_at** | **datetime** |  | 
**replacement** | [**ReplacementProvenance**](ReplacementProvenance.md) |  | [optional] 

## Example

```python
from tidal.models.installations_offline_inventory_resource_identifier_meta import InstallationsOfflineInventoryResourceIdentifierMeta

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsOfflineInventoryResourceIdentifierMeta from a JSON string
installations_offline_inventory_resource_identifier_meta_instance = InstallationsOfflineInventoryResourceIdentifierMeta.from_json(json)
# print the JSON string representation of the object
print(InstallationsOfflineInventoryResourceIdentifierMeta.to_json())

# convert the object into a dict
installations_offline_inventory_resource_identifier_meta_dict = installations_offline_inventory_resource_identifier_meta_instance.to_dict()
# create an instance of InstallationsOfflineInventoryResourceIdentifierMeta from a dict
installations_offline_inventory_resource_identifier_meta_from_dict = InstallationsOfflineInventoryResourceIdentifierMeta.from_dict(installations_offline_inventory_resource_identifier_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


