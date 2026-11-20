# CommentSummariesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | Number of existing comments directly targeting the subject. For a source file this counts root comments; for a comment this counts its direct replies. | 

## Example

```python
from tidal.models.comment_summaries_attributes import CommentSummariesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CommentSummariesAttributes from a JSON string
comment_summaries_attributes_instance = CommentSummariesAttributes.from_json(json)
# print the JSON string representation of the object
print(CommentSummariesAttributes.to_json())

# convert the object into a dict
comment_summaries_attributes_dict = comment_summaries_attributes_instance.to_dict()
# create an instance of CommentSummariesAttributes from a dict
comment_summaries_attributes_from_dict = CommentSummariesAttributes.from_dict(comment_summaries_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


