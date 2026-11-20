# VideosReplacementSingleRelationshipDataDocument

Target resource types: `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VideosReplacementResourceIdentifier**](VideosReplacementResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.videos_replacement_single_relationship_data_document import VideosReplacementSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideosReplacementSingleRelationshipDataDocument from a JSON string
videos_replacement_single_relationship_data_document_instance = VideosReplacementSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideosReplacementSingleRelationshipDataDocument.to_json())

# convert the object into a dict
videos_replacement_single_relationship_data_document_dict = videos_replacement_single_relationship_data_document_instance.to_dict()
# create an instance of VideosReplacementSingleRelationshipDataDocument from a dict
videos_replacement_single_relationship_data_document_from_dict = VideosReplacementSingleRelationshipDataDocument.from_dict(videos_replacement_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


