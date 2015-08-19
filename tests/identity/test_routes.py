from unittest import TestCase
from tests.helpers import setUpDB, setUpApp, tearDownDB
from tests.helpers import with_context, with_client
from lxml.html import document_fromstring
from app.identity.model import Identity


class TestRoutes(TestCase):

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    @with_client
    def test_get_list_identities(self, client):
        res = client.get('/identity')
        html = document_fromstring(res.get_data())

        header_exists = html.xpath('boolean(//tr/th)')
        self.assertTrue(header_exists)

        rows = html.xpath('boolean(//tr/td)')
        self.assertFalse(rows)

        joe = Identity()
        joe.save()
        john = Identity()
        john.save()
        jim = Identity()
        jim.save()

        res = client.get('/identity')
        html = document_fromstring(res.get_data())

        rows = html.xpath('boolean(//tr/td)')
        self.assertTrue(rows)

        ids = html.xpath('//tr/td[1]//text()')
        self.assertIn(str(joe.id), ids)

    @with_context
    @with_client
    def test_create_identity(self, client):
        all_before = Identity.all()

        res = client.post('/identity/new')
        self.assertEqual(302, res.status_code)

        all_after = Identity.all()

        new_identities = [iden for iden in all_after if iden not in all_before]
        self.assertTrue(len(new_identities) == 1)
