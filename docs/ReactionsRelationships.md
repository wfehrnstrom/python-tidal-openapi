# ReactionsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**ReactionsAuthorSingleRelationshipDataDocument**](ReactionsAuthorSingleRelationshipDataDocument.md) |  | [optional] 
**owners** | [**ReactionsOwnersMultiRelationshipDataDocument**](ReactionsOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**subject** | [**ReactionsSubjectSingleRelationshipDataDocument**](ReactionsSubjectSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.reactions_relationships import ReactionsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ReactionsRelationships from a JSON string
reactions_relationships_instance = ReactionsRelationships.from_json(json)
# print the JSON string representation of the object
print(ReactionsRelationships.to_json())

# convert the object into a dict
reactions_relationships_dict = reactions_relationships_instance.to_dict()
# create an instance of ReactionsRelationships from a dict
reactions_relationships_from_dict = ReactionsRelationships.from_dict(reactions_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


