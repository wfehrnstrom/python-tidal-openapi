# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from tidal.models.albums_album_statistics_single_relationship_data_document import AlbumsAlbumStatisticsSingleRelationshipDataDocument
from tidal.models.albums_artists_multi_relationship_data_document import AlbumsArtistsMultiRelationshipDataDocument
from tidal.models.albums_artists_relationship_update_operation_payload import AlbumsArtistsRelationshipUpdateOperationPayload
from tidal.models.albums_cover_art_multi_relationship_data_document import AlbumsCoverArtMultiRelationshipDataDocument
from tidal.models.albums_cover_art_relationship_update_operation_payload import AlbumsCoverArtRelationshipUpdateOperationPayload
from tidal.models.albums_create_operation_payload import AlbumsCreateOperationPayload
from tidal.models.albums_create_single_resource_data_document import AlbumsCreateSingleResourceDataDocument
from tidal.models.albums_genres_multi_relationship_data_document import AlbumsGenresMultiRelationshipDataDocument
from tidal.models.albums_items_multi_relationship_data_document import AlbumsItemsMultiRelationshipDataDocument
from tidal.models.albums_items_relationship_update_operation_payload import AlbumsItemsRelationshipUpdateOperationPayload
from tidal.models.albums_multi_resource_data_document import AlbumsMultiResourceDataDocument
from tidal.models.albums_owners_multi_relationship_data_document import AlbumsOwnersMultiRelationshipDataDocument
from tidal.models.albums_price_config_single_relationship_data_document import AlbumsPriceConfigSingleRelationshipDataDocument
from tidal.models.albums_providers_multi_relationship_data_document import AlbumsProvidersMultiRelationshipDataDocument
from tidal.models.albums_replacement_single_relationship_data_document import AlbumsReplacementSingleRelationshipDataDocument
from tidal.models.albums_shares_multi_relationship_data_document import AlbumsSharesMultiRelationshipDataDocument
from tidal.models.albums_similar_albums_multi_relationship_data_document import AlbumsSimilarAlbumsMultiRelationshipDataDocument
from tidal.models.albums_single_resource_data_document import AlbumsSingleResourceDataDocument
from tidal.models.albums_suggested_cover_arts_multi_relationship_data_document import AlbumsSuggestedCoverArtsMultiRelationshipDataDocument
from tidal.models.albums_update_operation_payload import AlbumsUpdateOperationPayload
from tidal.models.albums_usage_rules_single_relationship_data_document import AlbumsUsageRulesSingleRelationshipDataDocument
from tidal.models.default400_response_body import Default400ResponseBody
from tidal.models.default404_response_body import Default404ResponseBody
from tidal.models.default405_response_body import Default405ResponseBody
from tidal.models.default406_response_body import Default406ResponseBody
from tidal.models.default415_response_body import Default415ResponseBody
from tidal.models.default429_response_body import Default429ResponseBody
from tidal.models.default500_response_body import Default500ResponseBody
from tidal.models.default503_response_body import Default503ResponseBody
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody
from tidal.models.mutation_response_document import MutationResponseDocument
from tidal.security_api import get_token_Authorization_Code_PKCE, get_token_Client_Credentials

class BaseAlbumsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAlbumsApi.subclasses = BaseAlbumsApi.subclasses + (cls,)
    async def albums_get(
        self,
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        filter_barcode_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of barcode IDs (EAN-13 or UPC-A). NOTE: Supplying more than one barcode ID will currently only return one album per barcode ID. (e.g. `196589525444`)")],
        filter_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=20)]], Field(description="List of album IDs (e.g. `251380836`)")],
        filter_owners_id: Annotated[Optional[Annotated[List[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=1)]], Field(description="User id. Also accepts `me`.")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        sort: Annotated[Optional[List[str]], Field(description="Values prefixed with \"-\" are sorted descending; values without it are sorted ascending.")],
    ) -> AlbumsMultiResourceDataDocument:
        """Retrieves multiple albums by available filters, or without if applicable."""
        ...


    async def albums_post(
        self,
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        albums_create_operation_payload: Optional[AlbumsCreateOperationPayload],
    ) -> AlbumsCreateSingleResourceDataDocument:
        """Creates an uploaded album. Album creation is not atomic with its artist assignment, so the caller must be OWNER of every listed artist; COLLABORATOR, or a role on an album, is not enough until the album exists."""
        ...


    async def albums_id_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albumStatistics, artists, coverArt, genres, items, owners, priceConfig, providers, replacement, shares, similarAlbums, suggestedCoverArts, usageRules")],
        include_linkage: Annotated[Optional[List[str]], Field(description="Comma-separated direct relationships to return as linkage only, without related content.")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsSingleResourceDataDocument:
        """Retrieves single album by id."""
        ...


    async def albums_id_delete(
        self,
        id: Annotated[str, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> MutationResponseDocument:
        """Deletes existing album."""
        ...


    async def albums_id_patch(
        self,
        id: Annotated[str, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        albums_update_operation_payload: Optional[AlbumsUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Updates existing album. A COLLABORATOR on the album may update it; changing accessType, published or barcodeId needs OWNER."""
        ...


    async def albums_id_relationships_album_statistics_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: albumStatistics")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsAlbumStatisticsSingleRelationshipDataDocument:
        """Retrieves albumStatistics relationship."""
        ...


    async def albums_id_relationships_artists_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: artists")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: artists.albums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsArtistsMultiRelationshipDataDocument:
        """Retrieves artists relationship."""
        ...


    async def albums_id_relationships_artists_patch(
        self,
        id: Annotated[str, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        albums_artists_relationship_update_operation_payload: Optional[AlbumsArtistsRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Sets the album&#39;s artists, replacing the current list. Artists are listed in the order given. Provide 1 to 10 distinct artists. You can add your own artist profile and the profiles of users who have owner or collaborator access to the album. Owners and collaborators can change its artists. Returns an acknowledgement."""
        ...


    async def albums_id_relationships_cover_art_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: coverArt")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsCoverArtMultiRelationshipDataDocument:
        """Retrieves coverArt relationship."""
        ...


    async def albums_id_relationships_cover_art_patch(
        self,
        id: Annotated[str, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        albums_cover_art_relationship_update_operation_payload: Optional[AlbumsCoverArtRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Replaces the uploaded cover artwork selection with one attachable artwork. Empty data clears the selection. Previously attached uploaded artwork is soft-deleted unless system-managed. Returns an acknowledgement."""
        ...


    async def albums_id_relationships_genres_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: genres")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsGenresMultiRelationshipDataDocument:
        """Retrieves genres relationship."""
        ...


    async def albums_id_relationships_items_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: items")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: items")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsItemsMultiRelationshipDataDocument:
        """Retrieves items relationship."""
        ...


    async def albums_id_relationships_items_patch(
        self,
        id: Annotated[str, Field(description="Album id")],
        idempotency_key: Annotated[Optional[Annotated[str, Field(max_length=128)]], Field(description="Unique idempotency key for safe retry of mutation requests. If the same caller repeats a key with the same method, path, query and payload, the original response is replayed. If the request differs, a 422 error is returned.")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
        albums_items_relationship_update_operation_payload: Optional[AlbumsItemsRelationshipUpdateOperationPayload],
    ) -> MutationResponseDocument:
        """Incrementally updates one existing track&#39;s 1-based track number to meta.positionIndex. Does not replace the album&#39;s items or add or remove tracks. Empty data is rejected. A COLLABORATOR on the album may reorder. Returns an acknowledgement."""
        ...


    async def albums_id_relationships_owners_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: owners")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsOwnersMultiRelationshipDataDocument:
        """Retrieves owners relationship."""
        ...


    async def albums_id_relationships_price_config_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: priceConfig")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsPriceConfigSingleRelationshipDataDocument:
        """Retrieves priceConfig relationship."""
        ...


    async def albums_id_relationships_providers_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: providers")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsProvidersMultiRelationshipDataDocument:
        """Retrieves providers relationship."""
        ...


    async def albums_id_relationships_replacement_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: replacement")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: replacement")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsReplacementSingleRelationshipDataDocument:
        """Retrieves replacement relationship."""
        ...


    async def albums_id_relationships_shares_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: shares")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: shares.sharedResources")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsSharesMultiRelationshipDataDocument:
        """The album&#39;s share links, active and expired, newest first."""
        ...


    async def albums_id_relationships_similar_albums_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: similarAlbums")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        replace_media: Annotated[Optional[str], Field(description="Applies context-dependent replacements to media resource identifiers in selected relationships without changing stored data. Paths are comma-separated and follow `include` syntax. Example: similarAlbums")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsSimilarAlbumsMultiRelationshipDataDocument:
        """Retrieves similarAlbums relationship."""
        ...


    async def albums_id_relationships_suggested_cover_arts_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: suggestedCoverArts")],
        page_cursor: Annotated[Optional[str], Field(description="Server-generated cursor value pointing a certain page of items. Optional, targets first page if not specified")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsSuggestedCoverArtsMultiRelationshipDataDocument:
        """Retrieves suggestedCoverArts relationship."""
        ...


    async def albums_id_relationships_usage_rules_get(
        self,
        id: Annotated[str, Field(description="Album id")],
        country_code: Annotated[Optional[str], Field(description="ISO 3166-1 alpha-2 country code")],
        include: Annotated[Optional[List[str]], Field(description="Include related resources. Available relationships: usageRules")],
        share_code: Annotated[Optional[str], Field(description="Share code used as a bearer credential for the resource.")],
    ) -> AlbumsUsageRulesSingleRelationshipDataDocument:
        """Retrieves usageRules relationship."""
        ...
