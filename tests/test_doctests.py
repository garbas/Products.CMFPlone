"""
    CMFPlone doctests.  See also ``test_functional``.
"""

import os, sys

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from unittest import TestSuite
from Testing.ZopeTestCase import ZopeDocTestSuite
from Products.CMFPlone.tests import PloneTestCase
from Products.PloneTestCase.layer import ZCMLLayer
from Products.PloneTestCase import setup


def test_suite():
    suites = (
        ZopeDocTestSuite('Products.CMFPlone.CatalogTool',
                        test_class=PloneTestCase.FunctionalTestCase),
        ZopeDocTestSuite('Products.CMFPlone.PloneTool',
                         test_class=PloneTestCase.FunctionalTestCase),
        ZopeDocTestSuite('Products.CMFPlone.TranslationServiceTool',
                         test_class=PloneTestCase.FunctionalTestCase),
        ZopeDocTestSuite('Products.CMFPlone.CalendarTool',
                         test_class=PloneTestCase.FunctionalTestCase),
        ZopeDocTestSuite('Products.CMFPlone.utils'),
        )

    if setup.USELAYER:
        for s in suites:
            s.layer = ZCMLLayer

    return TestSuite(suites)

if __name__ == '__main__':
    framework()

