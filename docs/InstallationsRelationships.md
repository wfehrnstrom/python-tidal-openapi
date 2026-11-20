# InstallationsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offline_inventory** | [**InstallationsOfflineInventoryMultiRelationshipDataDocument**](InstallationsOfflineInventoryMultiRelationshipDataDocument.md) |  | [optional] 
**owners** | [**InstallationsOwnersMultiRelationshipDataDocument**](InstallationsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.installations_relationships import InstallationsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsRelationships from a JSON string
installations_relationships_instance = InstallationsRelationships.from_json(json)
# print the JSON string representation of the object
print(InstallationsRelationships.to_json())

# convert the object into a dict
installations_relationships_dict = installations_relationships_instance.to_dict()
# create an instance of InstallationsRelationships from a dict
installations_relationships_from_dict = InstallationsRelationships.from_dict(installations_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


