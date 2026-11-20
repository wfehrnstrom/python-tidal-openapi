# SharesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SharesAttributes**](SharesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SharesRelationships**](SharesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.shares_resource_object import SharesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SharesResourceObject from a JSON string
shares_resource_object_instance = SharesResourceObject.from_json(json)
# print the JSON string representation of the object
print(SharesResourceObject.to_json())

# convert the object into a dict
shares_resource_object_dict = shares_resource_object_instance.to_dict()
# create an instance of SharesResourceObject from a dict
shares_resource_object_from_dict = SharesResourceObject.from_dict(shares_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


