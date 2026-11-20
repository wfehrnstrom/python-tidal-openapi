# UsersArtistSingleRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.users_artist_single_relationship_data_document import UsersArtistSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UsersArtistSingleRelationshipDataDocument from a JSON string
users_artist_single_relationship_data_document_instance = UsersArtistSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(UsersArtistSingleRelationshipDataDocument.to_json())

# convert the object into a dict
users_artist_single_relationship_data_document_dict = users_artist_single_relationship_data_document_instance.to_dict()
# create an instance of UsersArtistSingleRelationshipDataDocument from a dict
users_artist_single_relationship_data_document_from_dict = UsersArtistSingleRelationshipDataDocument.from_dict(users_artist_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


