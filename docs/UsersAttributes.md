# UsersAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | ISO 3166-1 alpha-2 country code | 
**developer_access_tier** | **str** | Developer access tier for this user. | 
**email** | **str** | email address | [optional] 
**email_verified** | **bool** | Is the email verified | [optional] 
**first_name** | **str** | Users first name | [optional] 
**last_name** | **str** | Users last name | [optional] 
**nostr_public_key** | **str** | Users nostr public key | [optional] 
**username** | **str** | user name | 

## Example

```python
from tidal.models.users_attributes import UsersAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAttributes from a JSON string
users_attributes_instance = UsersAttributes.from_json(json)
# print the JSON string representation of the object
print(UsersAttributes.to_json())

# convert the object into a dict
users_attributes_dict = users_attributes_instance.to_dict()
# create an instance of UsersAttributes from a dict
users_attributes_from_dict = UsersAttributes.from_dict(users_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


