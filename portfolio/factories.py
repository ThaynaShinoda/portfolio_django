import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from portfolio.models import Project

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.user_name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
    slug = factory.LazyAttribute(lambda x: faker.slug())
    author = factory.SubFactory(UserFactory)
    description = factory.Faker('paragraph', nb_sentences=3)
    technologies = factory.LazyAttribute(lambda x: 'Python, Django, JavaScript')
    github_link = factory.LazyAttribute(lambda x: faker.url())
    created_on = factory.LazyAttribute(lambda x: now())
    updated_on = factory.LazyAttribute(lambda x: now())
    status = 1
