# TracksAlbumsMultiRelationshipDataDocument

Target resource types: `albums`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TracksAlbumsResourceIdentifier]**](TracksAlbumsResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_albums_multi_relationship_data_document import TracksAlbumsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksAlbumsMultiRelationshipDataDocument from a JSON string
tracks_albums_multi_relationship_data_document_instance = TracksAlbumsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksAlbumsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_albums_multi_relationship_data_document_dict = tracks_albums_multi_relationship_data_document_instance.to_dict()
# create an instance of TracksAlbumsMultiRelationshipDataDocument from a dict
tracks_albums_multi_relationship_data_document_from_dict = TracksAlbumsMultiRelationshipDataDocument.from_dict(tracks_albums_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


