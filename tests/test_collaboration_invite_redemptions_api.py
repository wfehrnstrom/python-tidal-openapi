# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.collaboration_invite_redemptions_create_operation_payload import CollaborationInviteRedemptionsCreateOperationPayload  # noqa: F401
from tidal.models.collaboration_invite_redemptions_create_single_resource_data_document import CollaborationInviteRedemptionsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.default400_response_body import Default400ResponseBody  # noqa: F401
from tidal.models.default404_response_body import Default404ResponseBody  # noqa: F401
from tidal.models.default405_response_body import Default405ResponseBody  # noqa: F401
from tidal.models.default406_response_body import Default406ResponseBody  # noqa: F401
from tidal.models.default415_response_body import Default415ResponseBody  # noqa: F401
from tidal.models.default429_response_body import Default429ResponseBody  # noqa: F401
from tidal.models.default500_response_body import Default500ResponseBody  # noqa: F401
from tidal.models.default503_response_body import Default503ResponseBody  # noqa: F401
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody  # noqa: F401
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody  # noqa: F401


def test_collaboration_invite_redemptions_post(client: TestClient):
    """Test case for collaboration_invite_redemptions_post

    Create single collaborationInviteRedemption.
    """
    collaboration_invite_redemptions_create_operation_payload = tidal.CollaborationInviteRedemptionsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/collaborationInviteRedemptions",
    #    headers=headers,
    #    json=collaboration_invite_redemptions_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

