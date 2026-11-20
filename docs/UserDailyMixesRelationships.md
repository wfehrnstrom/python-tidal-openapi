# UserDailyMixesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**UserDailyMixesItemsMultiRelationshipDataDocument**](UserDailyMixesItemsMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_daily_mixes_relationships import UserDailyMixesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserDailyMixesRelationships from a JSON string
user_daily_mixes_relationships_instance = UserDailyMixesRelationships.from_json(json)
# print the JSON string representation of the object
print(UserDailyMixesRelationships.to_json())

# convert the object into a dict
user_daily_mixes_relationships_dict = user_daily_mixes_relationships_instance.to_dict()
# create an instance of UserDailyMixesRelationships from a dict
user_daily_mixes_relationships_from_dict = UserDailyMixesRelationships.from_dict(user_daily_mixes_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


