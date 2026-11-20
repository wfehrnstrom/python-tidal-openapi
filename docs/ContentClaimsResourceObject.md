# ContentClaimsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ContentClaimsAttributes**](ContentClaimsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ContentClaimsRelationships**](ContentClaimsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.content_claims_resource_object import ContentClaimsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsResourceObject from a JSON string
content_claims_resource_object_instance = ContentClaimsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsResourceObject.to_json())

# convert the object into a dict
content_claims_resource_object_dict = content_claims_resource_object_instance.to_dict()
# create an instance of ContentClaimsResourceObject from a dict
content_claims_resource_object_from_dict = ContentClaimsResourceObject.from_dict(content_claims_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


