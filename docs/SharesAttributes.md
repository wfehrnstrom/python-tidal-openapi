# SharesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **List[str]** | Ways this share may be used to obtain access, decided by the server. Deprecated: clients must not rely on it. | 
**code** | **str** | Share code | 
**created_at** | **datetime** | Time the share was created. | 
**expires_at** | **datetime** | Time bearer access and acceptance expire; accepted grants remain valid. | 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | Links external to TIDAL API | [optional] 
**max_uses** | **int** | Number of saves the share permits. Absent when unlimited. | [optional] 
**password** | **str** | Password a user must send to save the share. Write-only: never returned. | [optional] 
**password_protected** | **bool** | Whether saving the share requires a password. A protected share never permits BEARER access, and only its owner and users with a role on its shared resource see that resource. | 
**role** | **str** | Role offered on the shared resource. | 
**use_count** | **int** | Number of saves so far, repeated saves included. Once it reaches maxUses, bearer access and acceptance end. Absent when maxUses is. | [optional] 

## Example

```python
from tidal.models.shares_attributes import SharesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SharesAttributes from a JSON string
shares_attributes_instance = SharesAttributes.from_json(json)
# print the JSON string representation of the object
print(SharesAttributes.to_json())

# convert the object into a dict
shares_attributes_dict = shares_attributes_instance.to_dict()
# create an instance of SharesAttributes from a dict
shares_attributes_from_dict = SharesAttributes.from_dict(shares_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


