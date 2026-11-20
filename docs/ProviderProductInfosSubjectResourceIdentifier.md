# ProviderProductInfosSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ProviderProductInfosSubjectResourceIdentifierMeta**](ProviderProductInfosSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.provider_product_infos_subject_resource_identifier import ProviderProductInfosSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderProductInfosSubjectResourceIdentifier from a JSON string
provider_product_infos_subject_resource_identifier_instance = ProviderProductInfosSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ProviderProductInfosSubjectResourceIdentifier.to_json())

# convert the object into a dict
provider_product_infos_subject_resource_identifier_dict = provider_product_infos_subject_resource_identifier_instance.to_dict()
# create an instance of ProviderProductInfosSubjectResourceIdentifier from a dict
provider_product_infos_subject_resource_identifier_from_dict = ProviderProductInfosSubjectResourceIdentifier.from_dict(provider_product_infos_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


