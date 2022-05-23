# django

from base.tests import BaseApiTestCase


class ListingCrudTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.listing = self.create_listing().json()

    def test_listing_create(self):
        data = {
            "name": "test",
            "description": "description",
            "image": self.create_temporary_image(),
            "price": 15,
            "publisher": self.user.get("id"),
        }

        response = self.create_listing(data)
        response_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data.get("name"), "test")
        self.assertEqual(response_data.get("description"), "description")
        self.assertEqual(response_data.get("price"), 15)
        self.assertEqual(response_data.get("publisher"), self.user.get("id"))

    def test_listing_update(self):
        response = self.client.put(
            f"/api/tool_listings/{self.listing.get('id')}/",
            {
                "name": "other",
                "description": "other",
                "price": 27,
                "image": self.create_temporary_image(),
                "publisher": self.listing.get("publisher"),
            },
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("name"), "other")
        self.assertEqual(data.get("description"), "other")
        self.assertEqual(data.get("price"), 27)
        self.assertEqual(data.get("publisher"), self.listing.get("publisher"))

    def test_listing_detail(self):
        response = self.client.get(f"/api/tool_listings/{self.listing.get('id')}/")
        data = response.json()
        self.assertIsNotNone(response.status_code, 200)
        self.assertIsNotNone(data.get("name"))
        self.assertIsNotNone(data.get("description"))
        self.assertIsNotNone(data.get("price"))
        self.assertIsNotNone(data.get("image"))
        self.assertIsNotNone(data.get("publisher"))

    def test_listing_delete(self):
        response = self.client.delete(f"/api/tool_listings/{self.listing.get('id')}/")
        self.assertEqual(response.status_code, 204)

    def test_listing_list(self):
        for _ in range(10):
            self.create_listing()

        response = self.client.get("/api/tool_listings/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 11)
