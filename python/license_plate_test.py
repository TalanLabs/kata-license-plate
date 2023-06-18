import unittest
from license_plate import next_license_plate


class LicensePlateTest(unittest.TestCase):

    def test_case_plus_five(self):
        license_plate = next_license_plate("AB-123-CD", 5)
        self.assertEqual(license_plate, "AB-128-CD")

    def test_case_plus_one_hundred(self):
        license_plate = next_license_plate("AZ-566-QS", 100)
        self.assertEqual(license_plate, "AZ-666-QS")

    def test_case_plus_one(self):
        license_plate = next_license_plate("BN-999-GH", 1)
        self.assertEqual(license_plate, "BN-001-GI")

    def test_case_plus_ten_thousand(self):
        license_plate = next_license_plate("CG-007-CG", 10000)
        self.assertEqual(license_plate, "CG-017-CQ")

    def test_case_plus_one_hundred_thousand(self):
        license_plate = next_license_plate("IO-010-OI", 100000)
        self.assertEqual(license_plate, "IO-110-SE")

    def test_case_plus_one_million(self):
        license_plate = next_license_plate("QS-456-DF", 1000000)
        self.assertEqual(license_plate, "QT-457-PS")