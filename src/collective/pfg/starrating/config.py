# -*- coding: utf-8 -*-
from Products.CMFCore.permissions import setDefaultRoles


PROJECTNAME = 'collective.pfg.starrating'
ADD_PERMISSIONS = {
    'FormStarRatingField': 'collective.pfg.starrating: Add FormStarRatingField',
}
setDefaultRoles(
    ADD_PERMISSIONS['FormStarRatingField'],
    ('Manager', 'Owner', 'Contributor', 'Site Administrator')
)
