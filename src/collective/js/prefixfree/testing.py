from plone.testing import z2
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.js.prefixfree


COLLECTIVE_JS_PREFIXFREE = PloneWithPackageLayer(
        zcml_package=collective.js.prefixfree,
        zcml_filename='testing.zcml',
        gs_profile_id='collective.js.prefixfree:testing',
        name='COLLECTIVE_JS_PREFIXFREE')

COLLECTIVE_JS_PREFIXFREE_INTEGRATION = IntegrationTesting(
                       bases=(COLLECTIVE_JS_PREFIXFREE, ),
                       name="COLLECTIVE_JS_PREFIXFREE_INTEGRATION")

COLLECTIVE_JS_PREFIXFREE_FUNCTIONAL = FunctionalTesting(
                       bases=(COLLECTIVE_JS_PREFIXFREE, ),
                       name="COLLECTIVE_JS_PREFIXFREE_FUNCTIONAL")

COLLECTIVE_JS_PREFIXFREE_ZSERVER = FunctionalTesting(
                       bases=(COLLECTIVE_JS_PREFIXFREE, z2.ZSERVER_FIXTURE),
                       name="COLLECTIVE_JS_PREFIXFREE_ZSERVER")
