from django.test import TestCase
from django.contrib.auth.models import User
from myblog.models import Post

class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

# and this test method to the PostTestCase
def test_string_representation(self):
    expected = "This is a title"
    p1 = Post(title=expected)
    actual = str(p1)
    self.assertEqual(expected, actual)
