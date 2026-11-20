# SavedSharesCreateResource403ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[SavedSharesCreateResource403ResponseBodyErrorsInner]**](SavedSharesCreateResource403ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.saved_shares_create_resource403_response_body import SavedSharesCreateResource403ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SavedSharesCreateResource403ResponseBody from a JSON string
saved_shares_create_resource403_response_body_instance = SavedSharesCreateResource403ResponseBody.from_json(json)
# print the JSON string representation of the object
print(SavedSharesCreateResource403ResponseBody.to_json())

# convert the object into a dict
saved_shares_create_resource403_response_body_dict = saved_shares_create_resource403_response_body_instance.to_dict()
# create an instance of SavedSharesCreateResource403ResponseBody from a dict
saved_shares_create_resource403_response_body_from_dict = SavedSharesCreateResource403ResponseBody.from_dict(saved_shares_create_resource403_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


