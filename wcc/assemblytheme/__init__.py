from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from five import grok

class HiddenProducts(grok.GlobalUtility):
    """This hides the upgrade profiles from the quick installer tool."""
    grok.implements(INonInstallable)
    grok.name('wcc.assemblytheme.upgrades')

    def getNonInstallableProducts(self):
        return [
            'wcc.assemblytheme.upgrades',
            ]
