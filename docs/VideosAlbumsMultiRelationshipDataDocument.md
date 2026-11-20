# VideosAlbumsMultiRelationshipDataDocument

Target resource types: `albums`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VideosAlbumsResourceIdentifier]**](VideosAlbumsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.videos_albums_multi_relationship_data_document import VideosAlbumsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideosAlbumsMultiRelationshipDataDocument from a JSON string
videos_albums_multi_relationship_data_document_instance = VideosAlbumsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideosAlbumsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
videos_albums_multi_relationship_data_document_dict = videos_albums_multi_relationship_data_document_instance.to_dict()
# create an instance of VideosAlbumsMultiRelationshipDataDocument from a dict
videos_albums_multi_relationship_data_document_from_dict = VideosAlbumsMultiRelationshipDataDocument.from_dict(videos_albums_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


