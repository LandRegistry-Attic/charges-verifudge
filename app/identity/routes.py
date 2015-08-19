from app.identity.model import Identity
from app.identity.views import ListIdentities, CreateIdentity
from flask import request, redirect, url_for


def register_routes(blueprint):

    @blueprint.route('/identity')
    def list_identities():
        all_identities = Identity.all()
        return ListIdentities(all_identities).render()

    @blueprint.route('/identity/new', methods=['POST', 'GET'])
    def create_identity():
        if request.method == 'GET':
            return CreateIdentity().render()
        elif request.method == 'POST':
            new_identity = Identity()
            new_identity.save()
            return redirect(url_for('identity.list_identities'))
