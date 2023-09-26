#!/usr/bin/env python
from flask import current_app as app
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

class UserSchema(ma.Schema):

    class Meta:
        fields = ('username', 'email')

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor('user', values=dict(id="<id>")),
            "collection": ma.URLFor('users'),
        }
    )

