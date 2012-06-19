import unittest2 as unittest

from plone.testing.z2 import Browser

from Products.CMFCore.utils import getToolByName

from collective.js.prefixfree.testing import (
    COLLECTIVE_JS_PREFIXFREE_FUNCTIONAL,
    COLLECTIVE_JS_PREFIXFREE_INTEGRATION)


class TestExample(unittest.TestCase):

    layer = COLLECTIVE_JS_PREFIXFREE_INTEGRATION

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'collective.js.prefixfree'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')


class TestJS(unittest.TestCase):

    layer = COLLECTIVE_JS_PREFIXFREE_FUNCTIONAL

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.js_tool = getToolByName(self.portal, 'portal_javascripts')
        self.js_tool.setDebugMode(True)
        import transaction
        transaction.commit()

    def test_js_is_included(self):
        browser = Browser(self.app)
        portalURL = self.portal.absolute_url()
        browser.open(portalURL)
        self.assertTrue(u"++resource++prefixfree/prefixfree.min.js"
                in browser.contents)

    def test_js_is_served(self):
        JS_URL = ("/portal_javascripts/Sunburst%20Theme/++resource++prefixfree"
            "/prefixfree.min.js")
        browser = Browser(self.app)
        portalURL = self.portal.absolute_url()
        browser.open(portalURL + JS_URL)
        self.assertTrue(u"Lea Verou" in browser.contents)
