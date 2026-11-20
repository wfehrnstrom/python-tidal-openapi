# ContentClaimsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assertion** | **str** | The claim assertion type | 
**created_at** | **datetime** | Timestamp when the claim was created | 
**last_modified_at** | **datetime** | Timestamp when the claim was last modified | 
**status** | **str** | Current status of this claim | 

## Example

```python
from tidal.models.content_claims_attributes import ContentClaimsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsAttributes from a JSON string
content_claims_attributes_instance = ContentClaimsAttributes.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsAttributes.to_json())

# convert the object into a dict
content_claims_attributes_dict = content_claims_attributes_instance.to_dict()
# create an instance of ContentClaimsAttributes from a dict
content_claims_attributes_from_dict = ContentClaimsAttributes.from_dict(content_claims_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


