# django

from base.tests import BaseApiTestCase


class ListingComplaintCrudTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.listing = self.create_listing().json()
        self.complaint = self.create_listing_complaint(
            {"listing": self.listing.get("id")}
        ).json()

    def test_listing_complaint_create(self):
        data = {
            "user_complainer": self.user.get("id"),
            "listing": self.listing.get("id"),
            "description": "test",
        }
        response = self.create_listing_complaint(data)
        response_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data.get("user_complainer"), self.user.get("id"))
        self.assertEqual(response_data.get("listing"), self.listing.get("id"))
        self.assertEqual(response_data.get("description"), "test")

    def test_listing_complaint_update(self):
        response = self.client.put(
            f"/api/complaints/{self.complaint.get('id')}/",
            {
                "user_complainer": self.user.get("id"),
                "listing": self.listing.get("id"),
                "description": "abc",
            },
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("user_complainer"), self.user.get("id"))
        self.assertEqual(data.get("listing"), self.listing.get("id"))
        self.assertEqual(data.get("description"), "abc")

    def test_listing_complaint_detail(self):
        response = self.client.get(f"/api/complaints/{self.complaint.get('id')}/")
        data = response.json()
        self.assertIsNotNone(data.get("user_complainer"))
        self.assertIsNotNone(data.get("listing"))
        self.assertIsNotNone(data.get("description"))

    def test_listing_complaint_delete(self):
        response = self.client.delete(f"/api/complaints/{self.complaint.get('id')}/")
        self.assertEqual(response.status_code, 204)

    def test_listing_complaint_list(self):
        for _ in range(10):
            self.create_listing_complaint()

        response = self.client.get("/api/complaints/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 11)
