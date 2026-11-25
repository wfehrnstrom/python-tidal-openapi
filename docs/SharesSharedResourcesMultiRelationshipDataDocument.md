# SharesSharedResourcesMultiRelationshipDataDocument

Target resource types: `albums`, `playlists`, `tracks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SharesSharedResourcesResourceIdentifier]**](SharesSharedResourcesResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.shares_shared_resources_multi_relationship_data_document import SharesSharedResourcesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SharesSharedResourcesMultiRelationshipDataDocument from a JSON string
shares_shared_resources_multi_relationship_data_document_instance = SharesSharedResourcesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(SharesSharedResourcesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
shares_shared_resources_multi_relationship_data_document_dict = shares_shared_resources_multi_relationship_data_document_instance.to_dict()
# create an instance of SharesSharedResourcesMultiRelationshipDataDocument from a dict
shares_shared_resources_multi_relationship_data_document_from_dict = SharesSharedResourcesMultiRelationshipDataDocument.from_dict(shares_shared_resources_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


