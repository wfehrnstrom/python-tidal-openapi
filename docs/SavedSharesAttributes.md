# SavedSharesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Time of this save (ISO 8601). Saving the share again returns the same id with the time of that request. | 

## Example

```python
from tidal.models.saved_shares_attributes import SavedSharesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSharesAttributes from a JSON string
saved_shares_attributes_instance = SavedSharesAttributes.from_json(json)
# print the JSON string representation of the object
print(SavedSharesAttributes.to_json())

# convert the object into a dict
saved_shares_attributes_dict = saved_shares_attributes_instance.to_dict()
# create an instance of SavedSharesAttributes from a dict
saved_shares_attributes_from_dict = SavedSharesAttributes.from_dict(saved_shares_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


