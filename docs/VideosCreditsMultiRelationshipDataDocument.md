# VideosCreditsMultiRelationshipDataDocument

Target resource types: `credits`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.videos_credits_multi_relationship_data_document import VideosCreditsMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VideosCreditsMultiRelationshipDataDocument from a JSON string
videos_credits_multi_relationship_data_document_instance = VideosCreditsMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(VideosCreditsMultiRelationshipDataDocument.to_json())

# convert the object into a dict
videos_credits_multi_relationship_data_document_dict = videos_credits_multi_relationship_data_document_instance.to_dict()
# create an instance of VideosCreditsMultiRelationshipDataDocument from a dict
videos_credits_multi_relationship_data_document_from_dict = VideosCreditsMultiRelationshipDataDocument.from_dict(videos_credits_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


