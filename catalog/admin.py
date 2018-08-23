from django.contrib import admin
from .models import Genre, Language, Book, BookInstance, Author

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.StackedInline):
    model = Book
    extra = 0


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    verbose_name = 'copy of this title'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]  # displayed horizontally when grouped in a tuple
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'lang')
    list_filter = ('author', 'lang')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Dislayed in list view
    list_display = ('id', 'book', 'borrower', 'media', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    # Display for a book instance
    fieldsets = (
        ('Book Information', {
            'fields': ('book', 'media', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower',)
        }),
    )
