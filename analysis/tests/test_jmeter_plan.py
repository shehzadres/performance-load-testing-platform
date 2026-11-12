import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

PLAN = Path(__file__).resolve().parents[2] / "jmeter" / "performance-test.jmx"


class JMeterPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = ET.parse(PLAN).getroot()

    def test_five_http_samplers_are_present(self):
        self.assertEqual(len(list(self.root.iter("HTTPSamplerProxy"))), 5)

    def test_every_sampler_has_a_response_assertion(self):
        parents = {child: parent for parent in self.root.iter() for child in parent}
        samplers = list(self.root.iter("HTTPSamplerProxy"))
        for sampler in samplers:
            siblings = list(parents[sampler])
            sampler_tree = siblings[siblings.index(sampler) + 1]
            self.assertEqual(sampler_tree.tag, "hashTree")
            self.assertEqual(len(list(sampler_tree.iter("ResponseAssertion"))), 1)

    def test_checkout_uses_post_and_expects_created(self):
        checkout = next(x for x in self.root.iter("HTTPSamplerProxy") if x.get("testname") == "Checkout")
        self.assertEqual(checkout.find("./stringProp[@name='HTTPSampler.method']").text, "POST")
        parents = {child: parent for parent in self.root.iter() for child in parent}
        siblings = list(parents[checkout])
        sampler_tree = siblings[siblings.index(checkout) + 1]
        expected = sampler_tree.find(".//ResponseAssertion/collectionProp/stringProp")
        self.assertEqual(expected.text, "201")


if __name__ == "__main__":
    unittest.main()
