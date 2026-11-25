"""
    TIDAL API

    The TIDAL API is a [JSON:API](https://jsonapi.org/)-compliant web API exposing TIDAL's music catalogue, metadata, and user functionality. Guides, authorization documentation, and API key management live at [developer.tidal.com](https://developer.tidal.com).  All endpoints exchange `application/vnd.api+json` documents per the [JSON:API specification](https://jsonapi.org/format/): [resource objects](https://jsonapi.org/format/#document-resource-objects) with `attributes` and `relationships`, [compound documents](https://jsonapi.org/format/#document-compound-documents) via `include`, and standard [error objects](https://jsonapi.org/format/#error-objects).  ### Authentication and authorization  Every request requires an OAuth 2.0 access token in the `Authorization: Bearer` header. Tokens are issued at `https://auth.tidal.com/v1/oauth2/token` via the client-credentials flow (server-to-server) or the authorization-code + PKCE flow (user context; authorize at `https://login.tidal.com/authorize`). Each endpoint documents which flows it accepts, the access tier it requires, and the scopes that apply. Scopes protect private user data: fields you are not authorized to read are redacted from the response rather than causing an error, and resources you cannot access at all behave as if they do not exist. See the [authorization guide](https://developer.tidal.com/documentation/api-sdk/api-sdk-authorization) for details.  ### Common wire types and compatibility  Each property's schema is authoritative for its allowed values, format, requiredness, nullability, and constraints. A standard defines how a value is represented; an individual schema may support only a documented subset.  - **Enums** use `UPPER_CASE_UNDERSCORE`, except JSON:API resource types, which use plural camelCase names such as `playlistGenerationSchedules`. New values can be added to any enum at any time, so treat unknown values as forward-compatible rather than errors. - **Resource IDs** are opaque strings. A few resources document well-known IDs for permanent system singleton instances; compare those IDs by exact value. Never parse, construct, or infer meaning from any other `id`, even when its current representation resembles an integer, UUID, or another recognizable value. Other properties explicitly marked with OpenAPI `format: uuid` are UUIDs. - **Dates and times** use ISO 8601. Date-times use the OpenAPI `date-time` format (`2024-05-01T12:00:00Z`), dates use `YYYY-MM-DD`, and durations use values such as `PT3M5S`. - **Recurrence frequencies** use RFC 5545 `FREQ` names such as `DAILY`, `WEEKLY`, and `MONTHLY`. The property's enum lists the frequencies that field currently supports. - **Weekdays** use `MONDAY` through `SUNDAY`. - **Time zones** use IANA Time Zone Database identifiers such as `Europe/Stockholm`, not abbreviations or raw UTC offsets for recurring civil-time schedules. - **Country codes** use ISO 3166-1 alpha-2; the shared country type also accepts `WW` for worldwide. **Locales** use IETF BCP 47 language tags such as `en-US`. - **Currencies** use ISO 4217 codes. Monetary amounts are decimal strings; each field defines its sign and precision constraints. - **Colors** use three- or six-digit hexadecimal strings (`#RGB` or `#RRGGBB`). Resource links to external URLs use JSON:API link objects with an `href` member.  ### Resource identifiers  Where supported, `filter[subject]=tracks:123` matches a related resource by type and ID; `filter[subject.id]=123` and `filter[subject.type]=tracks` match either component. Where multiple identifiers are accepted, comma-separated values match any complete pair. When a member path names a to-many relationship, at least one related resource must match; filtering does not trim that relationship. On collection and to-many relationship reads, the reserved root `self` (`filter[self]=tracks:123`) filters primary data itself. Each endpoint lists its supported filters and types.  Where supported, `me` aliases the authenticated user's dedicated resource ID for the referenced resource type. It works in paths, resource-ID filters, compact identifiers (`type:me`), resource PATCH primary IDs and standalone relationship mutation identifiers, with the same meaning as the resolved ID. Reads using the alias are `no-store`.  ### Relationships and includes  [Relationships](https://jsonapi.org/format/#document-resource-object-relationships) are returned only on request: [`include`](https://jsonapi.org/format/#fetching-includes) selects linkage and related content, while `includeLinkage` selects authorized linkage only. A relationship that was not requested is absent from the response, not empty. The full set of relationships a resource supports is documented in its schema.  For INTERNAL clients on resource GET endpoints, `includeLinkage` accepts comma-separated direct relationship names, for example `includeLinkage=subject,viewer`. It does not load related resources or add an `included` section. Nested paths and type qualifiers are unsupported. To-many linkage retains its normal pagination and relationship `next` links. Selecting the same relationship with both parameters applies full include behavior and reads the relationship once.  Request related resources in one round trip with `?include=`, a comma-separated list of dot-separated relationship paths — e.g. `include=coverArt,artists.profileArt` on an album. A nested path automatically embeds its intermediate resources: `artists.profileArt` includes the artists as well as their profile art. Include paths are always relative to the request's root resource, also on relationship endpoints. Including a relationship never changes the primary data; the related resources are added to `included`.  Include paths are validated: a path that cannot be resolved against the resources' documented relationships is rejected with `400`. Include trees are also bounded in path depth (default 3 levels) and in the total number of distinct resources they name (default 10); individual endpoints may apply different limits. Both selectors share the include-node limit, counting overlapping roots once. A request exceeding either limit is rejected with `400`, with the effective limit stated in the error.  ### Filtering, sorting, pagination  - [`filter[<memberPath>]=value`](https://jsonapi.org/format/#fetching-filtering) filters primary data by equality. Each endpoint lists its available filters; most collections require at least one. - Where explicitly documented, `filter[<memberPath>][ne]=value` negates the complete equality predicate. When the member path names a to-many relationship, no related ID may match any supplied value; a known-empty relationship matches. Operators are separate from values. Supplied comparisons combine with AND. For a required filter with multiple supported comparisons, at least one must be supplied; the parameter descriptions identify these alternatives. Unsupported operators and groups return `400`. - Where documented, `filter[<path>][<operator>]=value` applies an endpoint-defined operator, such as `filter[self][matchesQuery]`. Its meaning is described per endpoint, and it combines with other filters by AND. - [`sort=<memberPath>`](https://jsonapi.org/format/#fetching-sorting) sorts ascending, `-<memberPath>` descending (`sort=-addedAt`). Filter and sort member paths are relative to primary data. - Parameters an endpoint cannot honor are rejected with `400`: a `filter[...]` parameter the endpoint does not document (the error lists the available filters), or `sort` on an endpoint that documents no sort values. - [Pagination](https://jsonapi.org/format/#fetching-pagination) is cursor-based: responses carry `links.self` and, while more pages exist, `links.next` with an opaque `page[cursor]`. Follow `next` until absent — there are no offset or total-page parameters. Collection sizes, when available, appear as `meta.total` and may be approximate.  ### Type qualifiers  Where a relationship can contain several resource types, a path segment may be prefixed with a concrete type to scope which type's member is accessed. A playlist's `items` are `tracks` or `videos`: `GET /playlists/{id}?include=items.tracks:albums` resolves `albums` only for the items that are tracks. Qualifiers scope member access — they never filter which resources appear in a relationship — and can be chained.  The same syntax applies to `filter` and `sort` member paths on endpoints that support it; where supported, the qualified member is listed among the endpoint's documented filters and sort values. The syntax follows JSON:API proposal [json-api#1695](https://github.com/json-api/json-api/issues/1695).  ### Mutations  - [Partial updates](https://jsonapi.org/format/#crud-updating-resource-attributes) distinguish three wire states for nullable attributes: omission leaves the current value unchanged, an explicit `null` clears it, and a concrete value updates it. - Every mutation accepts an [`Idempotency-Key`](https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html) header. Keys are scoped to the client and the authenticated user. Once the original request has completed, retrying it with the same key, method, path, query and payload within one hour replays its response; a retry while it is still processing is rejected with `409`, and the same key with a different method, path, query or payload with `422`. - After a successful write, your own subsequent reads reflect the change; other clients may observe it with a delay.  ### Revisions and concurrent editing  Where supported, `attributes.revision` identifies the resource's documented aggregate state; a separately versioned relationship collection uses document `meta.revision`. Revisions are nonnegative integers that increase when covered state changes. Compare them only within the same identity and scope, preserve the exact value, and never calculate the next revision. Related content, viewer projections and independent sources are not automatically covered. Domain fields named `version`, such as a music edition, are distinct; existing endpoints retain their documented contracts.  Guarded mutations accept the observed value as top-level `meta.expectedRevision`. Each operation declares its scope and whether the precondition is required. A mismatch returns `409`; missing required input returns `400`. Refresh and reconcile after a conflict, then submit a new operation with a new idempotency key. An identical retry with the original key replays a recorded success under the idempotency contract. These revisions are not HTTP ETags.  Returned revisions describe observed snapshots, not reservations for later writes. Background changes can advance them immediately after a successful response.  ### Media resource replacements - BETA Internal only  Media resources (`tracks`, `videos`, and `albums`) can become unavailable in a country when licensing rights change. By default, TIDAL API returns the resource identifiers originally stored in a collection. This keeps ordinary reads predictable and consistent.  If a stored media resource is unavailable for the effective country, TIDAL may identify a contextually applicable alternative that is available there. Replacement is best effort, so an alternative is not always available. Replacement never changes the stored collection.  TIDAL API provides two ways to work with replacements:  1. **Inspect the `replacement` relationship.** A media resource can expose its applicable alternative through the `replacement` relationship. Include this relationship when a client needs both the original and replacement identifiers or wants to decide whether to use the replacement.  2. **Apply replacements with `replaceMedia`.** Clients can use `replaceMedia` to substitute applicable replacements directly into selected relationship data. The parameter accepts relationship paths using the same syntax as `include`. Projection affects only the response and preserves relationship order and metadata. Each identifier includes `meta.replacement` describing whether it was `ORIGINAL`, `REPLACED`, or `NOT_REPLACED`.  For example, `GET /playlists/{id}?include=items&replaceMedia=items` applies replacements to media identifiers in the playlist's `items` relationship.  ### Compression  Responses are gzip-compressed when the request includes `Accept-Encoding: gzip` (bodies over 2 KB).  ### Deprecation  Deprecated endpoints, parameters, and fields are marked `deprecated` in this specification, with the replacement noted in their description. Deprecated functionality keeps working for at least six months after being marked, and is only removed once a replacement is generally available.

    The version of the OpenAPI document: 1.10.263
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.artists_albums_multi_relationship_data_document import ArtistsAlbumsMultiRelationshipDataDocument
from tidal.models.artists_banner_art_multi_relationship_data_document import ArtistsBannerArtMultiRelationshipDataDocument
from tidal.models.artists_banner_art_relationship_update_operation_payload import ArtistsBannerArtRelationshipUpdateOperationPayload
from tidal.models.artists_biography_single_relationship_data_document import ArtistsBiographySingleRelationshipDataDocument
from tidal.models.artists_claim_status_single_relationship_data_document import ArtistsClaimStatusSingleRelationshipDataDocument
from tidal.models.artists_create_operation_payload import ArtistsCreateOperationPayload
from tidal.models.artists_followers_multi_relationship_data_document import ArtistsFollowersMultiRelationshipDataDocument
from tidal.models.artists_following_multi_relationship_data_document import ArtistsFollowingMultiRelationshipDataDocument
from tidal.models.artists_following_relationship_add_operation_payload import ArtistsFollowingRelationshipAddOperationPayload
from tidal.models.artists_following_relationship_remove_operation_payload import ArtistsFollowingRelationshipRemoveOperationPayload
from tidal.models.artists_logo_art_multi_relationship_data_document import ArtistsLogoArtMultiRelationshipDataDocument
from tidal.models.artists_logo_art_relationship_update_operation_payload import ArtistsLogoArtRelationshipUpdateOperationPayload
from tidal.models.artists_multi_resource_data_document import ArtistsMultiResourceDataDocument
from tidal.models.artists_owners_multi_relationship_data_document import ArtistsOwnersMultiRelationshipDataDocument
from tidal.models.artists_profile_art_multi_relationship_data_document import ArtistsProfileArtMultiRelationshipDataDocument
from tidal.models.artists_profile_art_relationship_update_operation_payload import ArtistsProfileArtRelationshipUpdateOperationPayload
from tidal.models.artists_radio_multi_relationship_data_document import ArtistsRadioMultiRelationshipDataDocument
from tidal.models.artists_roles_multi_relationship_data_document import ArtistsRolesMultiRelationshipDataDocument
from tidal.models.artists_similar_artists_multi_relationship_data_document import ArtistsSimilarArtistsMultiRelationshipDataDocument
from tidal.models.artists_single_resource_data_document import ArtistsSingleResourceDataDocument
from tidal.models.artists_track_providers_multi_relationship_data_document import ArtistsTrackProvidersMultiRelationshipDataDocument
from tidal.models.artists_tracks_multi_relationship_data_document import ArtistsTracksMultiRelationshipDataDocument
from tidal.models.artists_update_operation_payload import ArtistsUpdateOperationPayload
from tidal.models.artists_videos_multi_relationship_data_document import ArtistsVideosMultiRelationshipDataDocument
from tidal.models.mutation_response_document import MutationResponseDocument

from tidal.api_client import ApiClient, RequestSerialized
from tidal.api_response import ApiResponse
from tidal.rest import RESTResponseType


class ArtistsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def artists_get(
        self,
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        filter_handle: Annotated[Optional[List[Annotated[str, Field(min_length=1, strict=True)]]], Field(description="Artist handle (e.g. `jayz`)")] = None,
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of artist IDs (e.g. `1566`)")] = None,
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsMultiResourceDataDocument:
        """Get multiple artists.

        Retrieves multiple artists by available filters, or without if applicable.

        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param filter_handle: Artist handle (e.g. `jayz`)
        :type filter_handle: List[str]
        :param filter_id: List of artist IDs (e.g. `1566`)
        :type filter_id: List[str]
        :param filter_owners_id: User id. Also accepts `me`.
        :type filter_owners_id: List[str]
        :param include: Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_get_serialize(
            country_code=country_code,
            filter_handle=filter_handle,
            filter_id=filter_id,
            filter_owners_id=filter_owners_id,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsMultiResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_get_with_http_info(
        self,
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        filter_handle: Annotated[Optional[List[Annotated[str, Field(min_length=1, strict=True)]]], Field(description="Artist handle (e.g. `jayz`)")] = None,
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of artist IDs (e.g. `1566`)")] = None,
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsMultiResourceDataDocument]:
        """Get multiple artists.

        Retrieves multiple artists by available filters, or without if applicable.

        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param filter_handle: Artist handle (e.g. `jayz`)
        :type filter_handle: List[str]
        :param filter_id: List of artist IDs (e.g. `1566`)
        :type filter_id: List[str]
        :param filter_owners_id: User id. Also accepts `me`.
        :type filter_owners_id: List[str]
        :param include: Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_get_serialize(
            country_code=country_code,
            filter_handle=filter_handle,
            filter_id=filter_id,
            filter_owners_id=filter_owners_id,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsMultiResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_get_without_preload_content(
        self,
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        filter_handle: Annotated[Optional[List[Annotated[str, Field(min_length=1, strict=True)]]], Field(description="Artist handle (e.g. `jayz`)")] = None,
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=20)]], Field(description="List of artist IDs (e.g. `1566`)")] = None,
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get multiple artists.

        Retrieves multiple artists by available filters, or without if applicable.

        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param filter_handle: Artist handle (e.g. `jayz`)
        :type filter_handle: List[str]
        :param filter_id: List of artist IDs (e.g. `1566`)
        :type filter_id: List[str]
        :param filter_owners_id: User id. Also accepts `me`.
        :type filter_owners_id: List[str]
        :param include: Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_get_serialize(
            country_code=country_code,
            filter_handle=filter_handle,
            filter_id=filter_id,
            filter_owners_id=filter_owners_id,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsMultiResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_get_serialize(
        self,
        country_code,
        filter_handle,
        filter_id,
        filter_owners_id,
        include,
        include_linkage,
        replace_media,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'filter[handle]': 'multi',
            'filter[id]': 'multi',
            'filter[owners.id]': 'multi',
            'include': 'multi',
            'includeLinkage': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if filter_handle is not None:
            
            _query_params.append(('filter[handle]', filter_handle))
            
        if filter_id is not None:
            
            _query_params.append(('filter[id]', filter_id))
            
        if filter_owners_id is not None:
            
            _query_params.append(('filter[owners.id]', filter_owners_id))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if include_linkage is not None:
            
            _query_params.append(('includeLinkage', include_linkage))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsSingleResourceDataDocument:
        """Get single artist.

        Retrieves single artist by id.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsSingleResourceDataDocument]:
        """Get single artist.

        Retrieves single artist by id.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos")] = None,
        include_linkage: Annotated[Optional[List[StrictStr]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get single artist.

        Retrieves single artist by id.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albums, bannerArt, biography, claimStatus, followers, following, logoArt, owners, profileArt, radio, roles, similarArtists, trackProviders, tracks, videos
        :type include: List[str]
        :param include_linkage: Comma-separated direct relationships to return as linkage only, without related content.
        :type include_linkage: List[str]
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            include_linkage=include_linkage,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_get_serialize(
        self,
        id,
        country_code,
        include,
        include_linkage,
        replace_media,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
            'includeLinkage': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if include_linkage is not None:
            
            _query_params.append(('includeLinkage', include_linkage))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_patch(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_update_operation_payload: Optional[ArtistsUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Update single artist.

        When both profile colours are available, they must have at least 3:1 contrast.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_update_operation_payload:
        :type artists_update_operation_payload: ArtistsUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_update_operation_payload=artists_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_patch_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_update_operation_payload: Optional[ArtistsUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Update single artist.

        When both profile colours are available, they must have at least 3:1 contrast.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_update_operation_payload:
        :type artists_update_operation_payload: ArtistsUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_update_operation_payload=artists_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_patch_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_update_operation_payload: Optional[ArtistsUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update single artist.

        When both profile colours are available, they must have at least 3:1 contrast.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_update_operation_payload:
        :type artists_update_operation_payload: ArtistsUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_update_operation_payload=artists_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_patch_serialize(
        self,
        id,
        idempotency_key,
        artists_update_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if artists_update_operation_payload is not None:
            _body_params = artists_update_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/artists/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_albums_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsAlbumsMultiRelationshipDataDocument:
        """Get albums relationship (\"to-many\").

        Retrieves albums relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albums
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_albums_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsAlbumsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_albums_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsAlbumsMultiRelationshipDataDocument]:
        """Get albums relationship (\"to-many\").

        Retrieves albums relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albums
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_albums_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsAlbumsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_albums_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: albums")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get albums relationship (\"to-many\").

        Retrieves albums relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: albums
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_albums_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsAlbumsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_albums_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        replace_media,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/albums',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_banner_art_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: bannerArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsBannerArtMultiRelationshipDataDocument:
        """Get bannerArt relationship (\"to-many\").

        Reads the selected header banner artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: bannerArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_banner_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsBannerArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_banner_art_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: bannerArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsBannerArtMultiRelationshipDataDocument]:
        """Get bannerArt relationship (\"to-many\").

        Reads the selected header banner artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: bannerArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_banner_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsBannerArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_banner_art_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: bannerArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get bannerArt relationship (\"to-many\").

        Reads the selected header banner artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: bannerArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_banner_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsBannerArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_banner_art_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/bannerArt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_banner_art_patch(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_banner_art_relationship_update_operation_payload: Optional[ArtistsBannerArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Update bannerArt relationship (\"to-many\").

        Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_banner_art_relationship_update_operation_payload:
        :type artists_banner_art_relationship_update_operation_payload: ArtistsBannerArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_banner_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_banner_art_relationship_update_operation_payload=artists_banner_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_banner_art_patch_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_banner_art_relationship_update_operation_payload: Optional[ArtistsBannerArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Update bannerArt relationship (\"to-many\").

        Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_banner_art_relationship_update_operation_payload:
        :type artists_banner_art_relationship_update_operation_payload: ArtistsBannerArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_banner_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_banner_art_relationship_update_operation_payload=artists_banner_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_banner_art_patch_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_banner_art_relationship_update_operation_payload: Optional[ArtistsBannerArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update bannerArt relationship (\"to-many\").

        Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_banner_art_relationship_update_operation_payload:
        :type artists_banner_art_relationship_update_operation_payload: ArtistsBannerArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_banner_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_banner_art_relationship_update_operation_payload=artists_banner_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_banner_art_patch_serialize(
        self,
        id,
        idempotency_key,
        artists_banner_art_relationship_update_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if artists_banner_art_relationship_update_operation_payload is not None:
            _body_params = artists_banner_art_relationship_update_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/artists/{id}/relationships/bannerArt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_biography_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: biography")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsBiographySingleRelationshipDataDocument:
        """Get biography relationship (\"to-one\").

        Retrieves biography relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: biography
        :type include: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_biography_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsBiographySingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_biography_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: biography")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsBiographySingleRelationshipDataDocument]:
        """Get biography relationship (\"to-one\").

        Retrieves biography relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: biography
        :type include: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_biography_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsBiographySingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_biography_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: biography")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get biography relationship (\"to-one\").

        Retrieves biography relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: biography
        :type include: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_biography_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsBiographySingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_biography_get_serialize(
        self,
        id,
        country_code,
        include,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/biography',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_claim_status_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: claimStatus")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsClaimStatusSingleRelationshipDataDocument:
        """Get claimStatus relationship (\"to-one\").

        Retrieves claimStatus relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: claimStatus
        :type include: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_claim_status_get_serialize(
            id=id,
            include=include,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsClaimStatusSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_claim_status_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: claimStatus")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsClaimStatusSingleRelationshipDataDocument]:
        """Get claimStatus relationship (\"to-one\").

        Retrieves claimStatus relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: claimStatus
        :type include: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_claim_status_get_serialize(
            id=id,
            include=include,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsClaimStatusSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_claim_status_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: claimStatus")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get claimStatus relationship (\"to-one\").

        Retrieves claimStatus relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: claimStatus
        :type include: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_claim_status_get_serialize(
            id=id,
            include=include,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsClaimStatusSingleRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_claim_status_get_serialize(
        self,
        id,
        include,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/claimStatus',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_followers_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: followers")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums")] = None,
        viewer_context: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsFollowersMultiRelationshipDataDocument:
        """Get followers relationship (\"to-many\").

        Retrieves followers relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: followers
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums
        :type replace_media: str
        :param viewer_context:
        :type viewer_context: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_followers_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            viewer_context=viewer_context,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsFollowersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_followers_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: followers")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums")] = None,
        viewer_context: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsFollowersMultiRelationshipDataDocument]:
        """Get followers relationship (\"to-many\").

        Retrieves followers relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: followers
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums
        :type replace_media: str
        :param viewer_context:
        :type viewer_context: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_followers_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            viewer_context=viewer_context,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsFollowersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_followers_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: followers")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums")] = None,
        viewer_context: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get followers relationship (\"to-many\").

        Retrieves followers relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: followers
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: followers.albums
        :type replace_media: str
        :param viewer_context:
        :type viewer_context: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_followers_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            viewer_context=viewer_context,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsFollowersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_followers_get_serialize(
        self,
        id,
        include,
        page_cursor,
        replace_media,
        viewer_context,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if viewer_context is not None:
            
            _query_params.append(('viewerContext', viewer_context))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/followers',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_following_delete(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_following_relationship_remove_operation_payload: Optional[ArtistsFollowingRelationshipRemoveOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Delete from following relationship (\"to-many\").

        Deletes item(s) from following relationship.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_following_relationship_remove_operation_payload:
        :type artists_following_relationship_remove_operation_payload: ArtistsFollowingRelationshipRemoveOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_delete_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_following_relationship_remove_operation_payload=artists_following_relationship_remove_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_following_delete_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_following_relationship_remove_operation_payload: Optional[ArtistsFollowingRelationshipRemoveOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Delete from following relationship (\"to-many\").

        Deletes item(s) from following relationship.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_following_relationship_remove_operation_payload:
        :type artists_following_relationship_remove_operation_payload: ArtistsFollowingRelationshipRemoveOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_delete_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_following_relationship_remove_operation_payload=artists_following_relationship_remove_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_following_delete_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_following_relationship_remove_operation_payload: Optional[ArtistsFollowingRelationshipRemoveOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete from following relationship (\"to-many\").

        Deletes item(s) from following relationship.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_following_relationship_remove_operation_payload:
        :type artists_following_relationship_remove_operation_payload: ArtistsFollowingRelationshipRemoveOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_delete_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_following_relationship_remove_operation_payload=artists_following_relationship_remove_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_following_delete_serialize(
        self,
        id,
        idempotency_key,
        artists_following_relationship_remove_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if artists_following_relationship_remove_operation_payload is not None:
            _body_params = artists_following_relationship_remove_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/artists/{id}/relationships/following',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_following_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: following")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums")] = None,
        viewer_context: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsFollowingMultiRelationshipDataDocument:
        """Get following relationship (\"to-many\").

        Retrieves following relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: following
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums
        :type replace_media: str
        :param viewer_context:
        :type viewer_context: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            viewer_context=viewer_context,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsFollowingMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_following_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: following")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums")] = None,
        viewer_context: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsFollowingMultiRelationshipDataDocument]:
        """Get following relationship (\"to-many\").

        Retrieves following relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: following
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums
        :type replace_media: str
        :param viewer_context:
        :type viewer_context: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            viewer_context=viewer_context,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsFollowingMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_following_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: following")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums")] = None,
        viewer_context: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get following relationship (\"to-many\").

        Retrieves following relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: following
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: following.albums
        :type replace_media: str
        :param viewer_context:
        :type viewer_context: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            viewer_context=viewer_context,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsFollowingMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_following_get_serialize(
        self,
        id,
        include,
        page_cursor,
        replace_media,
        viewer_context,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        if viewer_context is not None:
            
            _query_params.append(('viewerContext', viewer_context))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/following',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_following_post(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_following_relationship_add_operation_payload: Optional[ArtistsFollowingRelationshipAddOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Add to following relationship (\"to-many\").

        Adds item(s) to following relationship.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_following_relationship_add_operation_payload:
        :type artists_following_relationship_add_operation_payload: ArtistsFollowingRelationshipAddOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_post_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_following_relationship_add_operation_payload=artists_following_relationship_add_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_following_post_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_following_relationship_add_operation_payload: Optional[ArtistsFollowingRelationshipAddOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Add to following relationship (\"to-many\").

        Adds item(s) to following relationship.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_following_relationship_add_operation_payload:
        :type artists_following_relationship_add_operation_payload: ArtistsFollowingRelationshipAddOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_post_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_following_relationship_add_operation_payload=artists_following_relationship_add_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_following_post_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_following_relationship_add_operation_payload: Optional[ArtistsFollowingRelationshipAddOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Add to following relationship (\"to-many\").

        Adds item(s) to following relationship.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_following_relationship_add_operation_payload:
        :type artists_following_relationship_add_operation_payload: ArtistsFollowingRelationshipAddOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_following_post_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_following_relationship_add_operation_payload=artists_following_relationship_add_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_following_post_serialize(
        self,
        id,
        idempotency_key,
        artists_following_relationship_add_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if artists_following_relationship_add_operation_payload is not None:
            _body_params = artists_following_relationship_add_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/artists/{id}/relationships/following',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_logo_art_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: logoArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsLogoArtMultiRelationshipDataDocument:
        """Get logoArt relationship (\"to-many\").

        Reads the selected logo artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: logoArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_logo_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsLogoArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_logo_art_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: logoArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsLogoArtMultiRelationshipDataDocument]:
        """Get logoArt relationship (\"to-many\").

        Reads the selected logo artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: logoArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_logo_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsLogoArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_logo_art_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: logoArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get logoArt relationship (\"to-many\").

        Reads the selected logo artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: logoArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_logo_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsLogoArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_logo_art_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/logoArt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_logo_art_patch(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_logo_art_relationship_update_operation_payload: Optional[ArtistsLogoArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Update logoArt relationship (\"to-many\").

        Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_logo_art_relationship_update_operation_payload:
        :type artists_logo_art_relationship_update_operation_payload: ArtistsLogoArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_logo_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_logo_art_relationship_update_operation_payload=artists_logo_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_logo_art_patch_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_logo_art_relationship_update_operation_payload: Optional[ArtistsLogoArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Update logoArt relationship (\"to-many\").

        Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_logo_art_relationship_update_operation_payload:
        :type artists_logo_art_relationship_update_operation_payload: ArtistsLogoArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_logo_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_logo_art_relationship_update_operation_payload=artists_logo_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_logo_art_patch_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_logo_art_relationship_update_operation_payload: Optional[ArtistsLogoArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update logoArt relationship (\"to-many\").

        Selects one owned, attachable IMAGE artwork by ID, replacing the selection. Empty data clears the selection; null data and more than one entry are rejected. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_logo_art_relationship_update_operation_payload:
        :type artists_logo_art_relationship_update_operation_payload: ArtistsLogoArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_logo_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_logo_art_relationship_update_operation_payload=artists_logo_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_logo_art_patch_serialize(
        self,
        id,
        idempotency_key,
        artists_logo_art_relationship_update_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if artists_logo_art_relationship_update_operation_payload is not None:
            _body_params = artists_logo_art_relationship_update_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/artists/{id}/relationships/logoArt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_owners_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: owners")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsOwnersMultiRelationshipDataDocument:
        """Get owners relationship (\"to-many\").

        Retrieves owners relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: owners
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_owners_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsOwnersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_owners_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: owners")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsOwnersMultiRelationshipDataDocument]:
        """Get owners relationship (\"to-many\").

        Retrieves owners relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: owners
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_owners_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsOwnersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_owners_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: owners")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get owners relationship (\"to-many\").

        Retrieves owners relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: owners
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_owners_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsOwnersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_owners_get_serialize(
        self,
        id,
        include,
        page_cursor,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/owners',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_profile_art_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: profileArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsProfileArtMultiRelationshipDataDocument:
        """Get profileArt relationship (\"to-many\").

        Reads the artist's avatar artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: profileArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_profile_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsProfileArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_profile_art_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: profileArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsProfileArtMultiRelationshipDataDocument]:
        """Get profileArt relationship (\"to-many\").

        Reads the artist's avatar artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: profileArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_profile_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsProfileArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_profile_art_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: profileArt")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get profileArt relationship (\"to-many\").

        Reads the artist's avatar artwork.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: profileArt
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_profile_art_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsProfileArtMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_profile_art_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/profileArt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_profile_art_patch(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_profile_art_relationship_update_operation_payload: Optional[ArtistsProfileArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Update profileArt relationship (\"to-many\").

        Replaces the artist's uploaded avatar selection with one owned, attachable artwork. Empty data clears the uploaded selection; legacy pictures or album fallback artwork may still appear in profileArt. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_profile_art_relationship_update_operation_payload:
        :type artists_profile_art_relationship_update_operation_payload: ArtistsProfileArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_profile_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_profile_art_relationship_update_operation_payload=artists_profile_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_profile_art_patch_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_profile_art_relationship_update_operation_payload: Optional[ArtistsProfileArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Update profileArt relationship (\"to-many\").

        Replaces the artist's uploaded avatar selection with one owned, attachable artwork. Empty data clears the uploaded selection; legacy pictures or album fallback artwork may still appear in profileArt. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_profile_art_relationship_update_operation_payload:
        :type artists_profile_art_relationship_update_operation_payload: ArtistsProfileArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_profile_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_profile_art_relationship_update_operation_payload=artists_profile_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_profile_art_patch_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_profile_art_relationship_update_operation_payload: Optional[ArtistsProfileArtRelationshipUpdateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update profileArt relationship (\"to-many\").

        Replaces the artist's uploaded avatar selection with one owned, attachable artwork. Empty data clears the uploaded selection; legacy pictures or album fallback artwork may still appear in profileArt. Previous artwork no longer selected by profileArt, bannerArt or logoArt is soft-deleted unless system-managed. Returns an acknowledgement.

        :param id: Artist id (required)
        :type id: str
        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_profile_art_relationship_update_operation_payload:
        :type artists_profile_art_relationship_update_operation_payload: ArtistsProfileArtRelationshipUpdateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_profile_art_patch_serialize(
            id=id,
            idempotency_key=idempotency_key,
            artists_profile_art_relationship_update_operation_payload=artists_profile_art_relationship_update_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_profile_art_patch_serialize(
        self,
        id,
        idempotency_key,
        artists_profile_art_relationship_update_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if artists_profile_art_relationship_update_operation_payload is not None:
            _body_params = artists_profile_art_relationship_update_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/artists/{id}/relationships/profileArt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_radio_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: radio")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsRadioMultiRelationshipDataDocument:
        """Get radio relationship (\"to-many\").

        Retrieves radio relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: radio
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_radio_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsRadioMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_radio_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: radio")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsRadioMultiRelationshipDataDocument]:
        """Get radio relationship (\"to-many\").

        Retrieves radio relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: radio
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_radio_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsRadioMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_radio_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: radio")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get radio relationship (\"to-many\").

        Retrieves radio relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: radio
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: radio.items
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_radio_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsRadioMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_radio_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        replace_media,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/radio',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_roles_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: roles")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsRolesMultiRelationshipDataDocument:
        """Get roles relationship (\"to-many\").

        Retrieves roles relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: roles
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_roles_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsRolesMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_roles_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: roles")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsRolesMultiRelationshipDataDocument]:
        """Get roles relationship (\"to-many\").

        Retrieves roles relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: roles
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_roles_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsRolesMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_roles_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: roles")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get roles relationship (\"to-many\").

        Retrieves roles relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: roles
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_roles_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsRolesMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_roles_get_serialize(
        self,
        id,
        include,
        page_cursor,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/roles',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_similar_artists_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: similarArtists")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsSimilarArtistsMultiRelationshipDataDocument:
        """Get similarArtists relationship (\"to-many\").

        Retrieves similarArtists relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: similarArtists
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_similar_artists_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsSimilarArtistsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_similar_artists_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: similarArtists")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsSimilarArtistsMultiRelationshipDataDocument]:
        """Get similarArtists relationship (\"to-many\").

        Retrieves similarArtists relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: similarArtists
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_similar_artists_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsSimilarArtistsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_similar_artists_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: similarArtists")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get similarArtists relationship (\"to-many\").

        Retrieves similarArtists relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: similarArtists
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarArtists.albums
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_similar_artists_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsSimilarArtistsMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_similar_artists_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        replace_media,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/similarArtists',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_track_providers_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: trackProviders")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsTrackProvidersMultiRelationshipDataDocument:
        """Get trackProviders relationship (\"to-many\").

        Retrieves trackProviders relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: trackProviders
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_track_providers_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsTrackProvidersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_track_providers_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: trackProviders")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsTrackProvidersMultiRelationshipDataDocument]:
        """Get trackProviders relationship (\"to-many\").

        Retrieves trackProviders relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: trackProviders
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_track_providers_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsTrackProvidersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_track_providers_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: trackProviders")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get trackProviders relationship (\"to-many\").

        Retrieves trackProviders relationship.

        :param id: Artist id (required)
        :type id: str
        :param include: Include related resources. Available relationships: trackProviders
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_track_providers_get_serialize(
            id=id,
            include=include,
            page_cursor=page_cursor,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsTrackProvidersMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_track_providers_get_serialize(
        self,
        id,
        include,
        page_cursor,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/trackProviders',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_tracks_get(
        self,
        collapse_by: Annotated[StrictStr, Field(description="Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items.")],
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: tracks")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsTracksMultiRelationshipDataDocument:
        """Get tracks relationship (\"to-many\").

        Retrieves tracks relationship.

        :param collapse_by: Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items. (required)
        :type collapse_by: str
        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: tracks
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_tracks_get_serialize(
            collapse_by=collapse_by,
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsTracksMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_tracks_get_with_http_info(
        self,
        collapse_by: Annotated[StrictStr, Field(description="Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items.")],
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: tracks")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsTracksMultiRelationshipDataDocument]:
        """Get tracks relationship (\"to-many\").

        Retrieves tracks relationship.

        :param collapse_by: Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items. (required)
        :type collapse_by: str
        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: tracks
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_tracks_get_serialize(
            collapse_by=collapse_by,
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsTracksMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_tracks_get_without_preload_content(
        self,
        collapse_by: Annotated[StrictStr, Field(description="Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items.")],
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: tracks")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get tracks relationship (\"to-many\").

        Retrieves tracks relationship.

        :param collapse_by: Collapse by options for getting artist tracks. Available options: FINGERPRINT, ID. FINGERPRINT option might collapse similar tracks based entry fingerprints while collapsing by ID always returns all available items. (required)
        :type collapse_by: str
        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: tracks
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: tracks
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_tracks_get_serialize(
            collapse_by=collapse_by,
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsTracksMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_tracks_get_serialize(
        self,
        collapse_by,
        id,
        country_code,
        include,
        page_cursor,
        replace_media,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if collapse_by is not None:
            
            _query_params.append(('collapseBy', collapse_by))
            
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/tracks',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_id_relationships_videos_get(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: videos")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ArtistsVideosMultiRelationshipDataDocument:
        """Get videos relationship (\"to-many\").

        Retrieves videos relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: videos
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_videos_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsVideosMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_id_relationships_videos_get_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: videos")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ArtistsVideosMultiRelationshipDataDocument]:
        """Get videos relationship (\"to-many\").

        Retrieves videos relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: videos
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_videos_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsVideosMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_id_relationships_videos_get_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Artist id")],
        country_code: Annotated[Optional[StrictStr], Field(description="ISO 3166-1 alpha-2 country code")] = None,
        include: Annotated[Optional[List[StrictStr]], Field(description="Include related resources. Available relationships: videos")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")] = None,
        replace_media: Annotated[Optional[StrictStr], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get videos relationship (\"to-many\").

        Retrieves videos relationship.

        :param id: Artist id (required)
        :type id: str
        :param country_code: ISO 3166-1 alpha-2 country code
        :type country_code: str
        :param include: Include related resources. Available relationships: videos
        :type include: List[str]
        :param page_cursor: Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified
        :type page_cursor: str
        :param replace_media: Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: videos
        :type replace_media: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_id_relationships_videos_get_serialize(
            id=id,
            country_code=country_code,
            include=include,
            page_cursor=page_cursor,
            replace_media=replace_media,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ArtistsVideosMultiRelationshipDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '415': "Default415ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_id_relationships_videos_get_serialize(
        self,
        id,
        country_code,
        include,
        page_cursor,
        replace_media,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'include': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if page_cursor is not None:
            
            _query_params.append(('page[cursor]', page_cursor))
            
        if replace_media is not None:
            
            _query_params.append(('replaceMedia', replace_media))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE', 
            'Client_Credentials'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/artists/{id}/relationships/videos',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def artists_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_create_operation_payload: Optional[ArtistsCreateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MutationResponseDocument:
        """Create single artist.

        Creates a new artist.

        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_create_operation_payload:
        :type artists_create_operation_payload: ArtistsCreateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_post_serialize(
            idempotency_key=idempotency_key,
            artists_create_operation_payload=artists_create_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '201': "ArtistsCreateSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def artists_post_with_http_info(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_create_operation_payload: Optional[ArtistsCreateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MutationResponseDocument]:
        """Create single artist.

        Creates a new artist.

        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_create_operation_payload:
        :type artists_create_operation_payload: ArtistsCreateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_post_serialize(
            idempotency_key=idempotency_key,
            artists_create_operation_payload=artists_create_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '201': "ArtistsCreateSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def artists_post_without_preload_content(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(strict=True, max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")] = None,
        artists_create_operation_payload: Optional[ArtistsCreateOperationPayload] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create single artist.

        Creates a new artist.

        :param idempotency_key: Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.
        :type idempotency_key: str
        :param artists_create_operation_payload:
        :type artists_create_operation_payload: ArtistsCreateOperationPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._artists_post_serialize(
            idempotency_key=idempotency_key,
            artists_create_operation_payload=artists_create_operation_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MutationResponseDocument",
            '201': "ArtistsCreateSingleResourceDataDocument",
            '400': "Default400ResponseBody",
            '404': "Default404ResponseBody",
            '405': "Default405ResponseBody",
            '406': "Default406ResponseBody",
            '409': "Idempotency409ResponseBody",
            '415': "Default415ResponseBody",
            '422': "Idempotency422ResponseBody",
            '429': "Default429ResponseBody",
            '500': "Default500ResponseBody",
            '503': "Default503ResponseBody",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _artists_post_serialize(
        self,
        idempotency_key,
        artists_create_operation_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Any] = self.api_client._merge_headers(_headers)
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            self.api_client._set_header(_header_params, 'Idempotency-Key', idempotency_key)
        # process the form parameters
        # process the body parameter
        if artists_create_operation_payload is not None:
            _body_params = artists_create_operation_payload


        # set the HTTP header `Accept`
        if not any(key.lower() == 'accept' for key in _header_params):
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.api+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            self.api_client._set_header(_header_params, 'Content-Type', _content_type)
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                self.api_client._set_header(_header_params, 'Content-Type', _default_content_type)

        # authentication setting
        _auth_settings: List[str] = [
            'Authorization_Code_PKCE'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/artists',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


