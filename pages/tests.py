from django.test import SimpleTestCase
from django.urls import reverse


#all tests must be prefixed with test_

class PageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_templates(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_uses_correct_templates(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_contains_string(self):
        response = self.client.get("/")
        self.assertContains(response, "Home Page")

    def test_about_page_contains_string(self):
        response = self.client.get("/about/")
        self.assertContains(response, "About us")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
