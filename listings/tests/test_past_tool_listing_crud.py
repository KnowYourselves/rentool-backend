# django

from base.tests import BaseApiTestCase


class PastListingCrudTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.listing = self.create_listing().json()
        self.past_listing = self.create_past_listing(
            {"listing": self.listing.get("id")}
        ).json()

    def test_past_listing_create(self):
        listing = self.create_listing().json()
        data = {
            "name": listing.get("name", "test"),
            "description": listing.get("description", "test"),
            "image": self.create_temporary_image(),
            "price": listing.get("price", 1),
            "listing": listing.get("id"),
            "renter": self.user.get("id"),
        }

        response = self.create_past_listing(data)
        response_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data.get("name"), "test")
        self.assertEqual(response_data.get("description"), "test")
        self.assertEqual(response_data.get("price"), 1)
        self.assertEqual(response_data.get("listing"), listing.get("id"))
        self.assertEqual(response_data.get("renter"), self.user.get("id"))

    def test_past_listing_update(self):
        response = self.client.put(
            f"/api/past-tool-listings/{self.past_listing.get('id')}/",
            {
                "name": "other",
                "description": "other",
                "price": 15,
                "image": self.create_temporary_image(),
                "listing": self.listing.get("id"),
                "renter": self.user.get("id"),
            },
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("name"), "other")
        self.assertEqual(data.get("description"), "other")
        self.assertEqual(data.get("price"), 15)

    def test_past_listing_detail(self):
        response = self.client.get(
            f"/api/past-tool-listings/{self.past_listing.get('id')}/"
        )
        data = response.json()
        self.assertIsNotNone(response.status_code, 200)
        self.assertIsNotNone(data.get("name"))
        self.assertIsNotNone(data.get("description"))
        self.assertIsNotNone(data.get("price"))
        self.assertIsNotNone(data.get("image"))

    def test_past_listing_delete(self):
        response = self.client.delete(
            f"/api/past-tool-listings/{self.past_listing.get('id')}/"
        )
        self.assertEqual(response.status_code, 204)

    def test_past_listing_list(self):
        for _ in range(10):
            self.create_past_listing()

        response = self.client.get("/api/past-tool-listings/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 11)
