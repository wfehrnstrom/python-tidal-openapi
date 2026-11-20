# InstallationsOfflineInventoryItemIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Also accepts &#x60;me&#x60; when type is &#x60;userCollectionTracks&#x60;. | 
**type** | **str** |  | 

## Example

```python
from tidal.models.installations_offline_inventory_item_identifier import InstallationsOfflineInventoryItemIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsOfflineInventoryItemIdentifier from a JSON string
installations_offline_inventory_item_identifier_instance = InstallationsOfflineInventoryItemIdentifier.from_json(json)
# print the JSON string representation of the object
print(InstallationsOfflineInventoryItemIdentifier.to_json())

# convert the object into a dict
installations_offline_inventory_item_identifier_dict = installations_offline_inventory_item_identifier_instance.to_dict()
# create an instance of InstallationsOfflineInventoryItemIdentifier from a dict
installations_offline_inventory_item_identifier_from_dict = InstallationsOfflineInventoryItemIdentifier.from_dict(installations_offline_inventory_item_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


