# UserDataExportsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**UserDataExportsOwnersMultiRelationshipDataDocument**](UserDataExportsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.user_data_exports_relationships import UserDataExportsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsRelationships from a JSON string
user_data_exports_relationships_instance = UserDataExportsRelationships.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsRelationships.to_json())

# convert the object into a dict
user_data_exports_relationships_dict = user_data_exports_relationships_instance.to_dict()
# create an instance of UserDataExportsRelationships from a dict
user_data_exports_relationships_from_dict = UserDataExportsRelationships.from_dict(user_data_exports_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


