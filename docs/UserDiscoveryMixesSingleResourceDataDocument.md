# UserDiscoveryMixesSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserDiscoveryMixesResourceObject**](UserDiscoveryMixesResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_discovery_mixes_single_resource_data_document import UserDiscoveryMixesSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserDiscoveryMixesSingleResourceDataDocument from a JSON string
user_discovery_mixes_single_resource_data_document_instance = UserDiscoveryMixesSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserDiscoveryMixesSingleResourceDataDocument.to_json())

# convert the object into a dict
user_discovery_mixes_single_resource_data_document_dict = user_discovery_mixes_single_resource_data_document_instance.to_dict()
# create an instance of UserDiscoveryMixesSingleResourceDataDocument from a dict
user_discovery_mixes_single_resource_data_document_from_dict = UserDiscoveryMixesSingleResourceDataDocument.from_dict(user_discovery_mixes_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


