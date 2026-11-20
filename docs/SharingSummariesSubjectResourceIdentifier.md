# SharingSummariesSubjectResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**SharingSummariesSubjectResourceIdentifierMeta**](SharingSummariesSubjectResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.sharing_summaries_subject_resource_identifier import SharingSummariesSubjectResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SharingSummariesSubjectResourceIdentifier from a JSON string
sharing_summaries_subject_resource_identifier_instance = SharingSummariesSubjectResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(SharingSummariesSubjectResourceIdentifier.to_json())

# convert the object into a dict
sharing_summaries_subject_resource_identifier_dict = sharing_summaries_subject_resource_identifier_instance.to_dict()
# create an instance of SharingSummariesSubjectResourceIdentifier from a dict
sharing_summaries_subject_resource_identifier_from_dict = SharingSummariesSubjectResourceIdentifier.from_dict(sharing_summaries_subject_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


