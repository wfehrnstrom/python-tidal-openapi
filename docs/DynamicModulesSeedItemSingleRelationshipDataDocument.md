# DynamicModulesSeedItemSingleRelationshipDataDocument

Target resource types: `albums`, `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DynamicModulesSeedItemResourceIdentifier**](DynamicModulesSeedItemResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dynamic_modules_seed_item_single_relationship_data_document import DynamicModulesSeedItemSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicModulesSeedItemSingleRelationshipDataDocument from a JSON string
dynamic_modules_seed_item_single_relationship_data_document_instance = DynamicModulesSeedItemSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(DynamicModulesSeedItemSingleRelationshipDataDocument.to_json())

# convert the object into a dict
dynamic_modules_seed_item_single_relationship_data_document_dict = dynamic_modules_seed_item_single_relationship_data_document_instance.to_dict()
# create an instance of DynamicModulesSeedItemSingleRelationshipDataDocument from a dict
dynamic_modules_seed_item_single_relationship_data_document_from_dict = DynamicModulesSeedItemSingleRelationshipDataDocument.from_dict(dynamic_modules_seed_item_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


