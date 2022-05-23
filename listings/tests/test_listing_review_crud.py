# django

from base.tests import BaseApiTestCase


class ListingReviewCrudTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.listing = self.create_listing().json()
        self.review = self.create_listing_review(
            {"listing": self.listing.get("id")}
        ).json()

    def test_listing_review_create(self):
        data = {
            "reviewer": self.user.get("id"),
            "listing": self.listing.get("id"),
            "score": 3,
            "description": "test",
        }
        response = self.create_listing_review(data)
        response_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data.get("reviewer"), self.user.get("id"))
        self.assertEqual(response_data.get("listing"), self.listing.get("id"))
        self.assertEqual(response_data.get("score"), 3)
        self.assertEqual(response_data.get("description"), "test")

    def test_listing_review_update(self):
        response = self.client.put(
            f"/api/reviews/{self.review.get('id')}/",
            {
                "reviewer": self.user.get("id"),
                "listing": self.listing.get("id"),
                "score": 1,
                "description": "abc",
            },
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("reviewer"), self.user.get("id"))
        self.assertEqual(data.get("listing"), self.listing.get("id"))
        self.assertEqual(data.get("score"), 1)
        self.assertEqual(data.get("description"), "abc")

    def test_listing_review_detail(self):
        response = self.client.get(f"/api/reviews/{self.review.get('id')}/")
        data = response.json()
        self.assertIsNotNone(data.get("reviewer"))
        self.assertIsNotNone(data.get("listing"))
        self.assertIsNotNone(data.get("score"))
        self.assertIsNotNone(data.get("description"))

    def test_listing_review_delete(self):
        response = self.client.delete(f"/api/reviews/{self.review.get('id')}/")
        self.assertEqual(response.status_code, 204)

    def test_listing_review_list(self):
        for _ in range(10):
            self.create_listing_review()

        response = self.client.get("/api/reviews/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 11)
