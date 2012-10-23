from five import grok
from Products.BlingPortlet.interfaces import ILinkableImage

grok.templatedir('templates')

class LinkableImageCarouselPortletView(grok.View):
    grok.template('linkableimage-carousel')
    grok.name('carousel-portlet-view')
    grok.context(ILinkableImage)
