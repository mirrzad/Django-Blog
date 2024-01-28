from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker
from ...models import Blog, Category


class Command(BaseCommand):
    help = "Create fake blogs for database"

    def __init__(self, *args, **kwargs):
        self.fake = Faker()
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        user = User.objects.create(username=self.fake.name(), password='f@ke123456')
        cat = Category.objects.create(title=self.fake.pystr(min_chars=5, max_chars=15))
        for _ in range(5):
            Blog.objects.create(
                title=self.fake.pystr(min_chars=5, max_chars=10),
                content=self.fake.paragraph(nb_sentences=5),
                is_active=True,
                author=user,
                category=cat
            )



