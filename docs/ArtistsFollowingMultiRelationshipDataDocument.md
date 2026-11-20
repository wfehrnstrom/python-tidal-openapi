# ArtistsFollowingMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsFollowingResourceIdentifier]**](ArtistsFollowingResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_following_multi_relationship_data_document import ArtistsFollowingMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsFollowingMultiRelationshipDataDocument from a JSON string
artists_following_multi_relationship_data_document_instance = ArtistsFollowingMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsFollowingMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_following_multi_relationship_data_document_dict = artists_following_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsFollowingMultiRelationshipDataDocument from a dict
artists_following_multi_relationship_data_document_from_dict = ArtistsFollowingMultiRelationshipDataDocument.from_dict(artists_following_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


