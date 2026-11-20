# DynamicPagesModulesMultiRelationshipDataDocument

Target resource types: `dynamicModules`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.dynamic_pages_modules_multi_relationship_data_document import DynamicPagesModulesMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPagesModulesMultiRelationshipDataDocument from a JSON string
dynamic_pages_modules_multi_relationship_data_document_instance = DynamicPagesModulesMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(DynamicPagesModulesMultiRelationshipDataDocument.to_json())

# convert the object into a dict
dynamic_pages_modules_multi_relationship_data_document_dict = dynamic_pages_modules_multi_relationship_data_document_instance.to_dict()
# create an instance of DynamicPagesModulesMultiRelationshipDataDocument from a dict
dynamic_pages_modules_multi_relationship_data_document_from_dict = DynamicPagesModulesMultiRelationshipDataDocument.from_dict(dynamic_pages_modules_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


