## Script (Python) "isIDAutoGenerated"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id=None
##title=
##
#autogenerated Ids look like $portal_type.YYYY-MM-DD.integer(random number)
from Products.CMFPlone.utils import log_deprecated
putils = context.plone_utils

if id is None:
    id=context.getId()

log_deprecated('The isIDAutoGenerated script is deprecated and will '
               'be removed in Plone 2.5. '
               'Please use the PloneTool method of the same name.')

return putils.isIDAutoGenerated(id)