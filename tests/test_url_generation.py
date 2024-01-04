from mboauth2 import AuthClient, Scope
from mboauth2.app import OAUTH_ENDPOINT

client = AuthClient(
    client_id="client_id",
    client_secret="client_secret",
    redirect_uri="https://example.com",
)


def test_generate_authorization_url():
    authorization_url = client.generate_auth_url(
        scopes=[Scope.PROFILE, Scope.EMAIL],
        state="state",
    )
    assert authorization_url.startswith(OAUTH_ENDPOINT)
    assert "scope=profile+email" in authorization_url
    assert "state=state" in authorization_url
