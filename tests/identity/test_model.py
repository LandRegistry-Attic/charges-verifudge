from unittest import TestCase
from tests.helpers import setUpDB, setUpApp, with_context, tearDownDB
from app.identity.model import Identity


class TestModel(TestCase):

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    def test_store_model(self):
        joe = Identity()

        self.assertEqual(joe.id, None)
        joe.save()
        self.assertNotEqual(joe.id, None)

        saved = Identity.get(joe.id)
        self.assertEqual(joe, saved)

    @with_context
    def test_get_all(self):
        self.assertEqual([], Identity.all())

        joe = Identity()
        joe.save()

        self.assertEqual([joe], Identity.all())

        jane = Identity()
        jane.save()

        self.assertListEqual([joe, jane], Identity.all())
