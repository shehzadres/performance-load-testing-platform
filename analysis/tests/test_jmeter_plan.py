import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

PLAN = Path(__file__).resolve().parents[2] / "jmeter" / "performance-test.jmx"


class JMeterPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = ET.parse(PLAN).getroot()
        cls.parents = {child: parent for parent in cls.root.iter() for child in parent}

    def test_five_http_samplers_are_present(self):
        self.assertEqual(len(list(self.root.iter("HTTPSamplerProxy"))), 5)

    def test_every_sampler_has_a_response_assertion(self):
        for sampler in self.root.iter("HTTPSamplerProxy"):
            siblings = list(self.parents[sampler])
            sampler_tree = siblings[siblings.index(sampler) + 1]
            self.assertEqual(sampler_tree.tag, "hashTree")
            self.assertEqual(len(list(sampler_tree.iter("ResponseAssertion"))), 1)

    def test_checkout_is_inside_transaction_controller_and_expects_created(self):
        checkout = next(x for x in self.root.iter("HTTPSamplerProxy") if x.get("testname") == "Checkout")
        controller = next(self.root.iter("TransactionController"))
        self.assertTrue(controller.get("testname", "").startswith("Transaction:"))
        controller_siblings = list(self.parents[controller])
        controller_tree = controller_siblings[controller_siblings.index(controller) + 1]
        self.assertIn(checkout, list(controller_tree))
        checkout_siblings = list(self.parents[checkout])
        checkout_tree = checkout_siblings[checkout_siblings.index(checkout) + 1]
        expected = checkout_tree.find(".//ResponseAssertion/collectionProp/stringProp")
        self.assertEqual(checkout.find("./stringProp[@name='HTTPSampler.method']").text, "POST")
        self.assertEqual(expected.text, "201")


if __name__ == "__main__":
    unittest.main()
