# ReactionsAuthorSingleRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.reactions_author_single_relationship_data_document import ReactionsAuthorSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsAuthorSingleRelationshipDataDocument from a JSON string
reactions_author_single_relationship_data_document_instance = ReactionsAuthorSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ReactionsAuthorSingleRelationshipDataDocument.to_json())

# convert the object into a dict
reactions_author_single_relationship_data_document_dict = reactions_author_single_relationship_data_document_instance.to_dict()
# create an instance of ReactionsAuthorSingleRelationshipDataDocument from a dict
reactions_author_single_relationship_data_document_from_dict = ReactionsAuthorSingleRelationshipDataDocument.from_dict(reactions_author_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


