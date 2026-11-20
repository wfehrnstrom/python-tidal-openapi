# UsersRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist** | [**UsersArtistSingleRelationshipDataDocument**](UsersArtistSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.users_relationships import UsersRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of UsersRelationships from a JSON string
users_relationships_instance = UsersRelationships.from_json(json)
# print the JSON string representation of the object
print(UsersRelationships.to_json())

# convert the object into a dict
users_relationships_dict = users_relationships_instance.to_dict()
# create an instance of UsersRelationships from a dict
users_relationships_from_dict = UsersRelationships.from_dict(users_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


