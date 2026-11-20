# ContentClaimsClaimedResourceResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ContentClaimsClaimedResourceResourceIdentifierMeta**](ContentClaimsClaimedResourceResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.content_claims_claimed_resource_resource_identifier import ContentClaimsClaimedResourceResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsClaimedResourceResourceIdentifier from a JSON string
content_claims_claimed_resource_resource_identifier_instance = ContentClaimsClaimedResourceResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsClaimedResourceResourceIdentifier.to_json())

# convert the object into a dict
content_claims_claimed_resource_resource_identifier_dict = content_claims_claimed_resource_resource_identifier_instance.to_dict()
# create an instance of ContentClaimsClaimedResourceResourceIdentifier from a dict
content_claims_claimed_resource_resource_identifier_from_dict = ContentClaimsClaimedResourceResourceIdentifier.from_dict(content_claims_claimed_resource_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


