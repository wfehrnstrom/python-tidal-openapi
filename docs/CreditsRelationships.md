# CreditsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist** | [**CreditsArtistSingleRelationshipDataDocument**](CreditsArtistSingleRelationshipDataDocument.md) |  | [optional] 
**category** | [**CreditsCategorySingleRelationshipDataDocument**](CreditsCategorySingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.credits_relationships import CreditsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsRelationships from a JSON string
credits_relationships_instance = CreditsRelationships.from_json(json)
# print the JSON string representation of the object
print(CreditsRelationships.to_json())

# convert the object into a dict
credits_relationships_dict = credits_relationships_instance.to_dict()
# create an instance of CreditsRelationships from a dict
credits_relationships_from_dict = CreditsRelationships.from_dict(credits_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


