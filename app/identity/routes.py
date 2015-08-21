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
            dob = "{day}-{month}-{year}".format(
                day=request.form.get('dob_day', None),
                month=request.form.get('dob_month', None),
                year=request.form.get('dob_year', None)
            )

            new_identity = Identity(
                first_name=request.form.get('first_name', None),
                middle_names=request.form.get('middle_names', None),
                last_name=request.form.get('last_name', None),
                dob=dob,
                address_line1=request.form.get('address_line1', None),
                address_line2=request.form.get('address_line2', None),
                address_line3=request.form.get('address_line3', None),
                address_line4=request.form.get('address_line4', None),
                address_line5=request.form.get('address_line5', None),
                postcode=request.form.get('postcode', None),
                gender=request.form.get('gender', None)
            )
            new_identity.save()
            return redirect(url_for('identity.list_identities'))
