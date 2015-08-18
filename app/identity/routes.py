from app.identity.model import Identity
from app.identity.views import ListIdentities


def register_routes(blueprint):

    @blueprint.route('/identity/list')
    def list_identities():
        all_identities = Identity.all()
        return ListIdentities(all_identities).render()
