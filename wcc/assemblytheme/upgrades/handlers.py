from Products.CMFCore.utils import getToolByName

def to1001(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.assemblytheme.upgrades:to1001')

