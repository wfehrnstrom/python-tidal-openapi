# ArtistStreamsStatisticsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdowns_status** | **str** | Status of artist statistics that may be withheld. OK: the data is present. SUPPRESSED: withheld because too few people are counted to show it. UNAVAILABLE: not available at the moment | 
**data_through** | **date** | Last day included in the underlying data | 
**end_date** | **date** | Last day of the window, inclusive | 
**last_modified_at** | **datetime** | When these statistics were computed | 
**listeners** | [**ArtistStreamsStatisticsCount**](ArtistStreamsStatisticsCount.md) |  | 
**new_followers** | [**ArtistStreamsStatisticsCount**](ArtistStreamsStatisticsCount.md) |  | 
**plays** | [**ArtistStreamsStatisticsPlays**](ArtistStreamsStatisticsPlays.md) |  | 
**plays_by_source** | [**ArtistStreamsStatisticsPlaysBySource**](ArtistStreamsStatisticsPlaysBySource.md) |  | [optional] 
**saves** | [**ArtistStreamsStatisticsCount**](ArtistStreamsStatisticsCount.md) |  | 
**series** | [**ArtistStreamsStatisticsSeries**](ArtistStreamsStatisticsSeries.md) |  | 
**start_date** | **date** | First day of the window | 
**top_countries** | [**ArtistStreamsStatisticsTopCountries**](ArtistStreamsStatisticsTopCountries.md) |  | [optional] 
**window_period** | [**ArtistStatisticsWindowPeriod**](ArtistStatisticsWindowPeriod.md) |  | 

## Example

```python
from tidal.models.artist_streams_statistics_attributes import ArtistStreamsStatisticsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsAttributes from a JSON string
artist_streams_statistics_attributes_instance = ArtistStreamsStatisticsAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsAttributes.to_json())

# convert the object into a dict
artist_streams_statistics_attributes_dict = artist_streams_statistics_attributes_instance.to_dict()
# create an instance of ArtistStreamsStatisticsAttributes from a dict
artist_streams_statistics_attributes_from_dict = ArtistStreamsStatisticsAttributes.from_dict(artist_streams_statistics_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


