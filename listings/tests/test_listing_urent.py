from base.tests import BaseApiTestCase
from listings.models import ToolListing


class ListingUnrentTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.listing = self.create_listing().json()

    def test_listing_unrent(self):
        self.rent_listing()
        self.assertEqual(
            ToolListing.objects.first().status,
            str(ToolListing.Status.RENTED),
        )

        response = self.client.patch(
            f"/api/tool-listings/{self.listing.get('id')}/unrent/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            ToolListing.objects.first().status,
            str(ToolListing.Status.PUBLISHED),
        )

    def test_cant_unrent_an_unrented_listing(self):
        response = self.client.patch(
            f"/api/tool-listings/{self.listing.get('id')}/unrent/"
        )
        self.assertEqual(response.status_code, 400)

    def rent_listing(self):
        ToolListing.objects.filter(id=self.listing.get("id")).update(
            status=ToolListing.Status.RENTED
        )
