from app.views.template import Template


class ListIdentities(Template):
    pageTitle = 'All Identities'

    def __init__(self, identities=[]):
        self.identities = identities


class CreateIdentity(Template):
    pageTitle = 'Create new Identity'
