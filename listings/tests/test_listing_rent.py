from base.tests import BaseApiTestCase
from listings.models import PastToolListing
from listings.models import ToolListing


class ListingRentTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.listing = self.create_listing().json()

    def test_listing_rent(self):
        response = self.client.patch(
            f"/api/tool-listings/{self.listing.get('id')}/rent/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            ToolListing.objects.first().status, str(ToolListing.Status.RENTED)
        )
        self.assertEqual(len(PastToolListing.objects.all()), 1)
        self.assertEqual(PastToolListing.objects.first().renter.id, self.user.get("id"))

    def test_cant_rent_a_rented_listing(self):
        self.client.patch(f"/api/tool-listings/{self.listing.get('id')}/rent/")
        response = self.client.patch(
            f"/api/tool-listings/{self.listing.get('id')}/rent/"
        )
        self.assertEqual(response.status_code, 400)
