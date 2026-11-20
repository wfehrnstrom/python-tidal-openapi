# ProviderProductInfosSubjectSingleRelationshipDataDocument

Target resource types: `albums`, `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProviderProductInfosSubjectResourceIdentifier**](ProviderProductInfosSubjectResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.provider_product_infos_subject_single_relationship_data_document import ProviderProductInfosSubjectSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderProductInfosSubjectSingleRelationshipDataDocument from a JSON string
provider_product_infos_subject_single_relationship_data_document_instance = ProviderProductInfosSubjectSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ProviderProductInfosSubjectSingleRelationshipDataDocument.to_json())

# convert the object into a dict
provider_product_infos_subject_single_relationship_data_document_dict = provider_product_infos_subject_single_relationship_data_document_instance.to_dict()
# create an instance of ProviderProductInfosSubjectSingleRelationshipDataDocument from a dict
provider_product_infos_subject_single_relationship_data_document_from_dict = ProviderProductInfosSubjectSingleRelationshipDataDocument.from_dict(provider_product_infos_subject_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


