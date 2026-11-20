# DownloadsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**DownloadsOwnersMultiRelationshipDataDocument**](DownloadsOwnersMultiRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.downloads_relationships import DownloadsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadsRelationships from a JSON string
downloads_relationships_instance = DownloadsRelationships.from_json(json)
# print the JSON string representation of the object
print(DownloadsRelationships.to_json())

# convert the object into a dict
downloads_relationships_dict = downloads_relationships_instance.to_dict()
# create an instance of DownloadsRelationships from a dict
downloads_relationships_from_dict = DownloadsRelationships.from_dict(downloads_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


