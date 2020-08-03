from unittest import TestCase

from Uop.dynamicattributes import DynamicAttributes


class TestDynamicAttributes(TestCase):
    def test_dynamicattributes(self):
        uio = DynamicAttributes("value")
        self.assertEqual(uio.attribute, "value")
        self.assertEqual(uio.fallback_xxx, "[fallback resolved] xxx")
        with self.assertRaisesRegex(AttributeError, ".* has no attribute \S+"):
            uio.randomattr



