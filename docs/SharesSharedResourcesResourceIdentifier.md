# SharesSharedResourcesResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**SharesSharedResourcesResourceIdentifierMeta**](SharesSharedResourcesResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.shares_shared_resources_resource_identifier import SharesSharedResourcesResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SharesSharedResourcesResourceIdentifier from a JSON string
shares_shared_resources_resource_identifier_instance = SharesSharedResourcesResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(SharesSharedResourcesResourceIdentifier.to_json())

# convert the object into a dict
shares_shared_resources_resource_identifier_dict = shares_shared_resources_resource_identifier_instance.to_dict()
# create an instance of SharesSharedResourcesResourceIdentifier from a dict
shares_shared_resources_resource_identifier_from_dict = SharesSharedResourcesResourceIdentifier.from_dict(shares_shared_resources_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


