import unittest
from app import prepare
class Tests(unittest.TestCase):
    def test_missing_fields_flagged(self): self.assertTrue(any(x["status"]=="missing" for x in prepare({})["checklist"]))
    def test_empty_allergy_list_is_explicit(self):
        item=next(x for x in prepare({"allergies":[]})["checklist"] if x["field"]=="allergies");self.assertEqual(item["status"],"ready")
if __name__=="__main__":unittest.main()
