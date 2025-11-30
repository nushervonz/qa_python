import pytest

from main import BooksCollector

class TestBooksCollector:
    
    def test_add_new_book_add_two_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate_book_not_added(self,collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_check_added_book_name(self,collector):
        collector.add_new_book('Hercules')
        assert 'Hercules' in collector.books_genre

    def test_add_new_book_not_add_empty_name(self,collector):
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    def test_add_new_book_with_41_characters_is_not_added(self,collector):
        long_name = 'A' * 41
        collector.add_new_book(long_name)
        assert len(collector.books_genre) == 0
    
    def test_add_new_book_with_40_characters_is_added(self,collector):
        long_valid_name = 'A' * 40
        collector.add_new_book(long_valid_name)
        assert long_valid_name in collector.books_genre
    
    @pytest.mark.parametrize('name, genre, expected_result',[
        ('Hercules', 'Фантастика', {'Hercules': 'Фантастика'}),
        ('Sherlock', 'Детективы', {'Sherlock': 'Детективы'}),
        ('Puaro', 'Детективы', {'Puaro': 'Детективы'}),
        ('Mickey Mouse', 'Мультфильмы', {'Mickey Mouse': 'Мультфильмы'}),
        ('Оно', 'Ужасы', {'Оно': 'Ужасы'}),
        ('Везунчик Джим', 'Комедии', {'Везунчик Джим': 'Комедии'}),
        ('Дюна', 'Фантастика', {'Дюна': 'Фантастика'})        
    ])
    def test_set_book_genre_valid_genre(self, collector, name, genre, expected_result):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre == expected_result
    
    @pytest.mark.parametrize('name, expected_genre',[('Hercules', 'Фантастика'), ('Sherlock', 'Детективы'),
        ('Puaro', 'Детективы'), 
        ('Mickey Mouse', 'Мультфильмы'), ('Оно', 'Ужасы'), 
        ('Везунчик Джим', 'Комедии'), ('Дюна', 'Фантастика')])
    def test_get_book_genre_returns_correct_genre(self, collector, name, expected_genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, expected_genre)
        assert collector.get_book_genre(name) == expected_genre
    
    @pytest.mark.parametrize('genre, expected_books',[('Фантастика', ['Hercules', 'Дюна']),
    ('Детективы', ['Sherlock', 'Puaro']),('Мультфильмы', ['Mickey Mouse']),
    ('Ужасы', ['Оно']),('Комедии', ['Везунчик Джим'])])
    def test_get_books_with_specific_genre_returns_correct_books(self, collector, genre, expected_books):
        books = {
            'Hercules': 'Фантастика',
            'Дюна': 'Фантастика',
            'Sherlock': 'Детективы',
            'Puaro': 'Детективы',
            'Mickey Mouse': 'Мультфильмы',
            'Оно': 'Ужасы',
            'Везунчик Джим': 'Комедии'
        }
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre_returns_correct_dictionary(self,collector):
        books = {
            'Hercules': 'Фантастика',
            'Дюна': 'Фантастика',
            'Sherlock': 'Детективы',
            'Puaro': 'Детективы',
            'Mickey Mouse': 'Мультфильмы',
            'Оно': 'Ужасы',
            'Везунчик Джим': 'Комедии'
            }
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
        collector.get_books_genre()
        assert collector.books_genre == books
        
    def test_get_books_for_children_returns_books_with_age_restriction(self,collector):
        books = {
                'Hercules': 'Фантастика',
                'Дюна': 'Фантастика',
                'Sherlock': 'Детективы',
                'Puaro': 'Детективы',
                'Mickey Mouse': 'Мультфильмы',
                'Оно': 'Ужасы',
                'Везунчик Джим': 'Комедии'
            }
        for name, book_genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
            collector.get_books_for_children()
        expected_children_books = ['Hercules', 'Дюна', 'Mickey Mouse', 'Везунчик Джим']
        assert collector.get_books_for_children() == expected_children_books

    @pytest.mark.parametrize('name',['Hercules', 'Sherlock',])
    def test_add_book_in_favorites_adds_books_to_favorites(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites
    
    def test_add_book_in_favorites_add_same_book_two_times_does_not_duplicate_book_in_favorites(self,collector):
        collector.add_new_book('Hercules')
        collector.add_book_in_favorites('Hercules')
        collector.add_book_in_favorites('Hercules')
        assert len(collector.favorites) == 1   
    
    def test_delete_book_from_favorites_removes_book_from_favorites(self,collector):
        
        collector.add_new_book('Hercules')
        collector.add_book_in_favorites('Hercules')
        collector.delete_book_from_favorites('Hercules')
        assert 'Hercules' not in collector.favorites