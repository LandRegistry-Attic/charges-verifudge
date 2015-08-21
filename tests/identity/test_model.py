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
        joe = Identity(
            first_name='Jane',
            middle_names='Jenny',
            last_name='Jones',
            dob='1-12-1988',
            address_line1='123 Fake Street',
            address_line2='Fakerton',
            address_line3='Fakesbury',
            address_line4='South Fakeshire',
            address_line5='Fakeland',
            postcode='AB12 3CD',
            gender='MALE'
        )

        self.assertEqual(joe.id, None)
        joe.save()
        self.assertNotEqual(joe.id, None)

        self.assertEquals(joe.first_name, 'Jane')
        self.assertEquals(joe.middle_names, 'Jenny')
        self.assertEquals(joe.last_name, 'Jones')
        self.assertEquals(joe.dob, '1-12-1988')
        self.assertEquals(joe.address_line1, '123 Fake Street')
        self.assertEquals(joe.address_line2, 'Fakerton')
        self.assertEquals(joe.address_line3, 'Fakesbury')
        self.assertEquals(joe.address_line4, 'South Fakeshire')
        self.assertEquals(joe.address_line5, 'Fakeland')
        self.assertEquals(joe.postcode, 'AB12 3CD')
        self.assertEquals(joe.gender, 'MALE')

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

    @with_context
    def test_tokens_are_generated(self):
        joe = Identity()
        jane = Identity()

        self.assertRegexpMatches(joe.token, '[A-Fa-f0-9]{7}')
        self.assertRegexpMatches(jane.token, '[A-Fa-f0-9]{7}')
        self.assertNotEquals(joe.token, jane.token)

    @with_context
    def test_empty_options(self):
        joe = Identity()
        joe.save()
        recovered = Identity.get(joe.id)

        self.assertEquals(recovered.first_name, None)
        self.assertEquals(recovered.middle_names, None)
        self.assertEquals(recovered.last_name, None)
        self.assertEquals(recovered.dob, None)
        self.assertEquals(recovered.address_line1, None)
        self.assertEquals(recovered.address_line2, None)
        self.assertEquals(recovered.address_line3, None)
        self.assertEquals(recovered.address_line4, None)
        self.assertEquals(recovered.address_line5, None)
        self.assertEquals(recovered.postcode, None)
        self.assertEquals(recovered.gender, None)

        self.assertNotEquals(recovered.token, None)
