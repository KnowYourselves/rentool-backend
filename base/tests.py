# standard library
import base64

from io import BytesIO

# django
from django.test import TestCase

# others libraries
from PIL import Image
from rest_framework.test import APIClient


class BaseApiTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self.create_user()
        self.credentials = self.get_credentials()
        self.set_credentials(self.credentials.get("access"))
        return super().setUp()

    def get_credentials(self, username="user", password="validpassword1"):
        return self.client.post(
            "/auth/jwt/create/",
            {"username": username, "password": password},
        ).json()

    def set_credentials(self, jwt):
        self.client.credentials(HTTP_AUTHORIZATION=f"JWT {jwt}")

    def create_temporary_image(self):
        bts = BytesIO()
        img = Image.new("RGB", (100, 100))
        img.save(bts, "jpeg")
        encoded = base64.b64encode(bts.getvalue()).decode("utf-8")
        return f"data:image/jpeg;base64,{encoded}"

    def create_user(
        self,
        username="user",
        password="validpassword1",
        email="example@example.com",
        phone_number="+56912345678",
    ):
        return self.client.post(
            "/auth/users/",
            {
                "username": username,
                "password": password,
                "email": email,
                "phone_number": phone_number,
            },
        ).json()

    def create_listing(self, data=None):
        data = data if data else {}
        return self.client.post(
            "/api/tool-listings/",
            {
                "name": data.get("name", "test"),
                "description": data.get("description", "test"),
                "image": data.get("image", self.create_temporary_image()),
                "price": data.get("price", 1),
                "publisher": data.get("publisher", self.user.get("id")),
            },
        )

    def create_past_listing(self, data=None):
        data = data if data else {}
        return self.client.post(
            "/api/past-tool-listings/",
            {
                "name": data.get("name", "test"),
                "description": data.get("description", "test"),
                "image": data.get("image", self.create_temporary_image()),
                "price": data.get("price", 1),
                "listing": data.get("listing", self.create_listing().json().get("id")),
                "renter": data.get("renter", self.user.get("id")),
            },
        )

    def create_listing_review(self, data=None):
        data = data if data else {}
        return self.client.post(
            "/api/reviews/",
            {
                "reviewer": data.get("reviewer", self.user.get("id")),
                "listing": data.get("listing", self.create_listing().json().get("id")),
                "score": data.get("score", 5),
                "description": data.get("description", "test"),
            },
        )

    def create_listing_complaint(self, data=None):
        data = data if data else {}
        return self.client.post(
            "/api/complaints/",
            {
                "user_complainer": data.get("user_complainer", self.user.get("id")),
                "listing": data.get("listing", self.create_listing().json().get("id")),
                "description": data.get("description", "test"),
            },
        )
