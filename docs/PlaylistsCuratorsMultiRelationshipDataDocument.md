# PlaylistsCuratorsMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.playlists_curators_multi_relationship_data_document import PlaylistsCuratorsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsCuratorsMultiRelationshipDataDocument from a JSON string
playlists_curators_multi_relationship_data_document_instance = PlaylistsCuratorsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(PlaylistsCuratorsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
playlists_curators_multi_relationship_data_document_dict = playlists_curators_multi_relationship_data_document_instance.to_dict()
# create an instance of PlaylistsCuratorsMultiRelationshipDataDocument from a dict
playlists_curators_multi_relationship_data_document_from_dict = PlaylistsCuratorsMultiRelationshipDataDocument.from_dict(playlists_curators_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


