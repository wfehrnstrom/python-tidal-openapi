# TracksRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**TracksAlbumsMultiRelationshipDataDocument**](TracksAlbumsMultiRelationshipDataDocument.md) |  | [optional] 
**artists** | [**TracksArtistsMultiRelationshipDataDocument**](TracksArtistsMultiRelationshipDataDocument.md) |  | [optional] 
**credits** | [**TracksCreditsMultiRelationshipDataDocument**](TracksCreditsMultiRelationshipDataDocument.md) |  | [optional] 
**download** | [**TracksDownloadSingleRelationshipDataDocument**](TracksDownloadSingleRelationshipDataDocument.md) |  | [optional] 
**genres** | [**TracksGenresMultiRelationshipDataDocument**](TracksGenresMultiRelationshipDataDocument.md) |  | [optional] 
**lyrics** | [**TracksLyricsMultiRelationshipDataDocument**](TracksLyricsMultiRelationshipDataDocument.md) |  | [optional] 
**metadata_status** | [**TracksMetadataStatusSingleRelationshipDataDocument**](TracksMetadataStatusSingleRelationshipDataDocument.md) |  | [optional] 
**owners** | [**TracksOwnersMultiRelationshipDataDocument**](TracksOwnersMultiRelationshipDataDocument.md) |  | [optional] 
**price_config** | [**TracksPriceConfigSingleRelationshipDataDocument**](TracksPriceConfigSingleRelationshipDataDocument.md) |  | [optional] 
**providers** | [**TracksProvidersMultiRelationshipDataDocument**](TracksProvidersMultiRelationshipDataDocument.md) |  | [optional] 
**radio** | [**TracksRadioMultiRelationshipDataDocument**](TracksRadioMultiRelationshipDataDocument.md) |  | [optional] 
**replacement** | [**TracksReplacementSingleRelationshipDataDocument**](TracksReplacementSingleRelationshipDataDocument.md) |  | [optional] 
**shares** | [**TracksSharesMultiRelationshipDataDocument**](TracksSharesMultiRelationshipDataDocument.md) |  | [optional] 
**similar_tracks** | [**TracksSimilarTracksMultiRelationshipDataDocument**](TracksSimilarTracksMultiRelationshipDataDocument.md) |  | [optional] 
**source_file** | [**TracksSourceFileSingleRelationshipDataDocument**](TracksSourceFileSingleRelationshipDataDocument.md) |  | [optional] 
**suggested_tracks** | [**TracksSuggestedTracksMultiRelationshipDataDocument**](TracksSuggestedTracksMultiRelationshipDataDocument.md) |  | [optional] 
**track_statistics** | [**TracksTrackStatisticsSingleRelationshipDataDocument**](TracksTrackStatisticsSingleRelationshipDataDocument.md) |  | [optional] 
**usage_rules** | [**TracksUsageRulesSingleRelationshipDataDocument**](TracksUsageRulesSingleRelationshipDataDocument.md) |  | [optional] 

## Example

```python
from tidal.models.tracks_relationships import TracksRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TracksRelationships from a JSON string
tracks_relationships_instance = TracksRelationships.from_json(json)
# print the JSON string representation of the object
print(TracksRelationships.to_json())

# convert the object into a dict
tracks_relationships_dict = tracks_relationships_instance.to_dict()
# create an instance of TracksRelationships from a dict
tracks_relationships_from_dict = TracksRelationships.from_dict(tracks_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


