# SharingSummariesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared** | **bool** | Whether a live grant to another user, an unexpired bearer grant or an applicable undeleted, unexpired share exists on the subject or an ancestor. Everyone grants do not count. Ancestor folder links require VOUCHER; exhausted links still count. | 
**shared_via_parent** | **bool** | The same sharing check restricted to ancestor folders and albums. Descendants never contribute. | 

## Example

```python
from tidal.models.sharing_summaries_attributes import SharingSummariesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SharingSummariesAttributes from a JSON string
sharing_summaries_attributes_instance = SharingSummariesAttributes.from_json(json)
# print the JSON string representation of the object
print(SharingSummariesAttributes.to_json())

# convert the object into a dict
sharing_summaries_attributes_dict = sharing_summaries_attributes_instance.to_dict()
# create an instance of SharingSummariesAttributes from a dict
sharing_summaries_attributes_from_dict = SharingSummariesAttributes.from_dict(sharing_summaries_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


