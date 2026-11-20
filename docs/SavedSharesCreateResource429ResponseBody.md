# SavedSharesCreateResource429ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[SavedSharesCreateResource429ResponseBodyErrorsInner]**](SavedSharesCreateResource429ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.saved_shares_create_resource429_response_body import SavedSharesCreateResource429ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSharesCreateResource429ResponseBody from a JSON string
saved_shares_create_resource429_response_body_instance = SavedSharesCreateResource429ResponseBody.from_json(json)
# print the JSON string representation of the object
print(SavedSharesCreateResource429ResponseBody.to_json())

# convert the object into a dict
saved_shares_create_resource429_response_body_dict = saved_shares_create_resource429_response_body_instance.to_dict()
# create an instance of SavedSharesCreateResource429ResponseBody from a dict
saved_shares_create_resource429_response_body_from_dict = SavedSharesCreateResource429ResponseBody.from_dict(saved_shares_create_resource429_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


