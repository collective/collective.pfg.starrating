# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from collective.pfg.starrating import config
from Products.Archetypes import atapi
from Products.ATContentTypes.content.base import registerATCT
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName
from Products.PloneFormGen.content.fieldsBase import BaseFieldSchemaStringDefault
from Products.PloneFormGen.content.fieldsBase import BaseFormField
from Products.PloneFormGen.content.fieldsBase import finalizeFieldSchema
from Products.PloneFormGen.content.fieldsBase import StringVocabularyField
from Products.PloneFormGen.content.fieldsBase import vocabularyField
from Products.PloneFormGen.content.fieldsBase import vocabularyOverrideField

starrating_schema = BaseFieldSchemaStringDefault.copy() + atapi.Schema((
    vocabularyField,
    vocabularyOverrideField,
))

del starrating_schema['hidden']
del starrating_schema['serverSide']

finalizeFieldSchema(starrating_schema, folderish=True, moveDiscussion=False)


class FormStarRatingField(BaseFormField):
    """ Star Rating Field (radio buttons or select) """

    meta_type = 'FormStarRatingField'
    security = ClassSecurityInfo()
    schema = starrating_schema

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        # set a preconfigured field as an instance attribute
        self.fgField = StringVocabularyField(
            'fg_starrating_field',
            searchable=0,
            required=0,
            widget=atapi.SelectionWidget(
                macro="pfg_starrating"
            ),
            vocabulary='_get_selection_vocab',
            enforceVocabulary=1,
            write_permission=View,
        )


    def htmlValue(self, REQUEST):
        """ Return value instead of key """

        utils = getToolByName(self, 'plone_utils')
        charset = utils.getSiteEncoding()

        value = REQUEST.form.get(self.__name__, '')

        # note that vocabulary items are in unicode;
        # so, we must decode before lookup
        vu = value.decode(charset)

        vocabulary = self.fgField.Vocabulary(self)
        voc = vocabulary.getValue(vu) or vu

        return cgi.escape(voc.encode(charset))

    def exclude_from_nav(self):
        return True

registerATCT(FormStarRatingField, config.PROJECTNAME)
