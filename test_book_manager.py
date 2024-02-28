import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book("1234567890", "Book1", "Author1")
        self.book2 = Book("0987654321", "Book2", "Author2")

    def test_add_book(self):
        self.manager.add_book(self.book1)
        self.assertIn(self.book1, self.manager.books)

        self.manager.add_book(self.book2)
        self.assertIn(self.book2, self.manager.books)

        initial_count = len(self.manager.books)
        self.manager.add_book(self.book1)
        self.assertEqual(len(self.manager.books), initial_count)

    def test_remove_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book("1234567890")
        self.assertNotIn(self.book1, self.manager.books)

        initial_count = len(self.manager.books)
        self.manager.remove_book("0987654321")
        self.assertEqual(len(self.manager.books), initial_count)

    def test_list_books(self):
        self.assertEqual(len(self.manager.list_books()), 0)

        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        books = self.manager.list_books()
        self.assertEqual(len(books), 2)
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)

    def test_remove_nonexistent_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book("0987654321")
        self.assertIn(self.book1, self.manager.books)

    def test_add_duplicate_book(self):
        self.manager.add_book(self.book1)
        initial_count = len(self.manager.books)
        self.manager.add_book(self.book1)
        self.assertEqual(len(self.manager.books), initial_count)

    def test_add_remove_multiple_books(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.assertEqual(len(self.manager.books), 2)

        self.manager.remove_book("1234567890")
        self.assertNotIn(self.book1, self.manager.books)
        self.assertEqual(len(self.manager.books), 1)

        self.manager.remove_book("0987654321")
        self.assertNotIn(self.book2, self.manager.books)
        self.assertEqual(len(self.manager.books), 0)

    def test_remove_all_books(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.assertEqual(len(self.manager.books), 2)

        self.manager.remove_book("1234567890")
        self.manager.remove_book("0987654321")
        self.assertEqual(len(self.manager.books), 0)

    def test_list_books_empty_manager(self):
        self.assertEqual(len(self.manager.list_books()), 0)

if __name__ == '__main__':
    unittest.main()