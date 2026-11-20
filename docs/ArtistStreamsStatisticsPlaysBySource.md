# ArtistStreamsStatisticsPlaysBySource

Plays by where they started. other holds the plays not in items. Without a note, items and other add up to all plays, and an absent other means no plays are left. With note HIDDEN, part of the plays is withheld, so an absent other is unknown rather than zero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ArtistStreamsStatisticsSourcePlays]**](ArtistStreamsStatisticsSourcePlays.md) |  | 
**note** | **str** | How a breakdown relates to its total. GROUPED: the remainder includes entries too small to show alone, and the breakdown still adds up to the total. HIDDEN: part of the total is withheld, so the breakdown adds up to less than the total. UNKNOWN: a note this API does not know, so the breakdown may not add up | [optional] 
**other** | [**ArtistStreamsStatisticsOtherPlays**](ArtistStreamsStatisticsOtherPlays.md) |  | [optional] 

## Example

```python
from tidal.models.artist_streams_statistics_plays_by_source import ArtistStreamsStatisticsPlaysBySource

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsPlaysBySource from a JSON string
artist_streams_statistics_plays_by_source_instance = ArtistStreamsStatisticsPlaysBySource.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsPlaysBySource.to_json())

# convert the object into a dict
artist_streams_statistics_plays_by_source_dict = artist_streams_statistics_plays_by_source_instance.to_dict()
# create an instance of ArtistStreamsStatisticsPlaysBySource from a dict
artist_streams_statistics_plays_by_source_from_dict = ArtistStreamsStatisticsPlaysBySource.from_dict(artist_streams_statistics_plays_by_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


