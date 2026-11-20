# InstallationsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.installations_owners_multi_relationship_data_document import InstallationsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationsOwnersMultiRelationshipDataDocument from a JSON string
installations_owners_multi_relationship_data_document_instance = InstallationsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(InstallationsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
installations_owners_multi_relationship_data_document_dict = installations_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of InstallationsOwnersMultiRelationshipDataDocument from a dict
installations_owners_multi_relationship_data_document_from_dict = InstallationsOwnersMultiRelationshipDataDocument.from_dict(installations_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


