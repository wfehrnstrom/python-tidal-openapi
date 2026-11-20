# SharingSummariesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SharingSummariesAttributes**](SharingSummariesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SharingSummariesRelationships**](SharingSummariesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.sharing_summaries_resource_object import SharingSummariesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SharingSummariesResourceObject from a JSON string
sharing_summaries_resource_object_instance = SharingSummariesResourceObject.from_json(json)
# print the JSON string representation of the object
print(SharingSummariesResourceObject.to_json())

# convert the object into a dict
sharing_summaries_resource_object_dict = sharing_summaries_resource_object_instance.to_dict()
# create an instance of SharingSummariesResourceObject from a dict
sharing_summaries_resource_object_from_dict = SharingSummariesResourceObject.from_dict(sharing_summaries_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


