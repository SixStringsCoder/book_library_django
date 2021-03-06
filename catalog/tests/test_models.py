from django.test import TestCase
from catalog.models import Author, Genre, Language, Book, BookInstance


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'Born')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='Y Is for Yesterday')

    def test_title_label(self):
        title = Book.objects.get(id=1)
        field_label = title._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_author_label(self):
        author = Book.objects.get(id=1)
        field_label = author._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_summary_label(self):
        summary = Book.objects.get(id=1)
        field_label = summary._meta.get_field('summary').verbose_name
        self.assertEqual(field_label, 'summary')

    def test_isbn_label(self):
        isbn = Book.objects.get(id=1)
        field_label = isbn._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_genre_label(self):
        genre = Book.objects.get(id=1)
        field_label = genre._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'genre')

    def test_lang_label(self):
        lang = Book.objects.get(id=1)
        field_label = lang._meta.get_field('lang').verbose_name
        self.assertEqual(field_label, 'lang')

    def test_title_max_length(self):
        title = Book.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_summary_max_length(self):
        summary = Book.objects.get(id=1)
        max_length = summary._meta.get_field('summary').max_length
        self.assertEqual(max_length, 1000)

    def test_isbn_max_length(self):
        isbn = Book.objects.get(id=1)
        max_length = isbn._meta.get_field('isbn').max_length
        self.assertEqual(max_length, 13)


class BookInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        BookInstance.objects.create(id='04a77f53-172c-4579-9a39-64e7cc30fd66')

    def test_bookinstance_id_help_text(self):
        id = BookInstance.objects.get(id='04a77f53-172c-4579-9a39-64e7cc30fd66')
        help_text = id._meta.get_field('id').help_text
        self.assertEqual(help_text, 'Unique library ID for this book')

    def test_bookinstance_media_help_text(self):
        media = BookInstance.objects.get(id='04a77f53-172c-4579-9a39-64e7cc30fd66')
        help_text = media._meta.get_field('media').help_text
        self.assertEqual(help_text, 'Type of media (e.g. hardback, audiobook)')

    def test_bookinstance_max_lengthl(self):
        media = BookInstance.objects.get(id='04a77f53-172c-4579-9a39-64e7cc30fd66')
        max_length = media._meta.get_field('media').max_length
        self.assertEqual(max_length, 200)


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Science Fiction')

    def test_genre_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_genre_name_help_text(self):
        name = Genre.objects.get(id=1)
        help_text = name._meta.get_field('name').help_text
        self.assertEqual(help_text, 'Enter a book genre (e.g. Science Fiction, Mystery, etc.)')


class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='Farsi')

    def test_language_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertLessEqual(max_length, 25)

    def test_langauge_name_help_text(self):
        name = Language.objects.get(id=1)
        help_text = name._meta.get_field('name').help_text
        self.assertEqual(help_text, 'Enter the language the book is written in (e.g. Chinese, Farsi).')
