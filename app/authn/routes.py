from app.authn import views


def register_routes(blueprint):
    @blueprint.route('/fake-authn-request')
    def fake_authn_request_maker():
        return views.FakeAuthnRequest().render()
