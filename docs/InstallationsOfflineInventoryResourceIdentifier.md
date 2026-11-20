# InstallationsOfflineInventoryResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**InstallationsOfflineInventoryResourceIdentifierMeta**](InstallationsOfflineInventoryResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.installations_offline_inventory_resource_identifier import InstallationsOfflineInventoryResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsOfflineInventoryResourceIdentifier from a JSON string
installations_offline_inventory_resource_identifier_instance = InstallationsOfflineInventoryResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(InstallationsOfflineInventoryResourceIdentifier.to_json())

# convert the object into a dict
installations_offline_inventory_resource_identifier_dict = installations_offline_inventory_resource_identifier_instance.to_dict()
# create an instance of InstallationsOfflineInventoryResourceIdentifier from a dict
installations_offline_inventory_resource_identifier_from_dict = InstallationsOfflineInventoryResourceIdentifier.from_dict(installations_offline_inventory_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


