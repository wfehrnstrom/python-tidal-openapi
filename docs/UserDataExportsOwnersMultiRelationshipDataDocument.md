# UserDataExportsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_data_exports_owners_multi_relationship_data_document import UserDataExportsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataExportsOwnersMultiRelationshipDataDocument from a JSON string
user_data_exports_owners_multi_relationship_data_document_instance = UserDataExportsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserDataExportsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
user_data_exports_owners_multi_relationship_data_document_dict = user_data_exports_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of UserDataExportsOwnersMultiRelationshipDataDocument from a dict
user_data_exports_owners_multi_relationship_data_document_from_dict = UserDataExportsOwnersMultiRelationshipDataDocument.from_dict(user_data_exports_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


