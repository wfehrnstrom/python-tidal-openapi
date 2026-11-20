# UserOfflineMixesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserOfflineMixesItemsMultiRelationshipDataDocument**](UserOfflineMixesItemsMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_offline_mixes_relationships import UserOfflineMixesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserOfflineMixesRelationships from a JSON string
user_offline_mixes_relationships_instance = UserOfflineMixesRelationships.from_json(json)
# print the JSON string representation of the object
print(UserOfflineMixesRelationships.to_json())

# convert the object into a dict
user_offline_mixes_relationships_dict = user_offline_mixes_relationships_instance.to_dict()
# create an instance of UserOfflineMixesRelationships from a dict
user_offline_mixes_relationships_from_dict = UserOfflineMixesRelationships.from_dict(user_offline_mixes_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


