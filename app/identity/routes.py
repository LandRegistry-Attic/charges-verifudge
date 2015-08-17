from app.identity.model import Identity


def register_routes(blueprint):

    @blueprint.route('/identity/list')
    def list_identities():
        joe = Identity()
        return "foo" + joe.id
