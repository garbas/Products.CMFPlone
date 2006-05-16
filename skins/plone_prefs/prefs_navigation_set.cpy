## Controller Script (Python) "prefs_navigation_set"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=generated_tabs=False, portaltypes=[], enable_wf_state_filtering=False, wf_states_to_show=[], bottomLevel=0, name='Navigation', root='/', currentFolderOnlyInNavtree=False, topLevel=0, RESPONSE=None
##title=Set Navigation Prefs
##

from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFCore.utils import getToolByName

REQUEST=context.REQUEST
portal_properties=getToolByName(context, 'portal_properties')

if generated_tabs:
  portal_properties.site_properties.manage_changeProperties(disable_folder_sections=False)
else:
  portal_properties.site_properties.manage_changeProperties(disable_folder_sections=True)

# The menu pretends to be a whitelist, but we are storing a blacklist so that
# new types are searchable by default. Inverse the list.
allTypes = context.getPortalTypes()
blacklistedTypes = [t for t in allTypes if t not in portaltypes]

bottomLevel = int(bottomLevel)
topLevel = int(topLevel)

portal_properties.navtree_properties.manage_changeProperties(
                        metaTypesNotToList=blacklistedTypes,
                        enable_wf_state_filtering=enable_wf_state_filtering,
                        wf_states_to_show=wf_states_to_show,
                        name=name,
                        root=root,
                        currentFolderOnlyInNavtree=currentFolderOnlyInNavtree,
                        topLevel=topLevel,
                        bottomLevel=bottomLevel)

context.plone_utils.addPortalMessage(_(u'Navigation settings updated.'))
return state