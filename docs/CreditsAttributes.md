# CreditsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Credit name | 
**role** | **str** | Credit role | 

## Example

```python
from tidal.models.credits_attributes import CreditsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsAttributes from a JSON string
credits_attributes_instance = CreditsAttributes.from_json(json)
# print the JSON string representation of the object
print(CreditsAttributes.to_json())

# convert the object into a dict
credits_attributes_dict = credits_attributes_instance.to_dict()
# create an instance of CreditsAttributes from a dict
credits_attributes_from_dict = CreditsAttributes.from_dict(credits_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


