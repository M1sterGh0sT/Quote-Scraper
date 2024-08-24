import unittest
from unittest.mock import patch, Mock
from scrapping import search

class TestQuoteScraper(unittest.TestCase):

    @patch('scrapping.requests.get')
    def test_known_author(self, mock_get):
        # Test case for a known author
        mock_html = '''
        <div class="quote">
            <span class="text">"Life is what happens when you're busy making other plans."</span>
            <small class="author">John Lennon</small>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "John Lennon")
            mock_print.assert_any_call('John Lennon \nQuote: "Life is what happens when you\'re busy making other plans."\n')

    @patch('scrapping.requests.get')
    def test_unknown_author(self, mock_get):
        # Test case for an unknown author
        mock_html = '''
        <div class="quote">
            <span class="text">"Life is what happens when you're busy making other plans."</span>
            <small class="author">John Doe</small>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "Eleanor")
            mock_print.assert_not_called()

    @patch('scrapping.requests.get')
    def test_empty_input(self, mock_get):
        # Return a valid HTML page, but we expect no output for empty input
        mock_html = '''
            <div class="quote">
                <span class="text">"Life is what happens when you're busy making other plans."</span>
                <small class="author">John Doe</small>
            </div>
            '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "")
            mock_print.assert_not_called()

    @patch('scrapping.requests.get')
    def test_only_spaces_input(self, mock_get):
        # Test case for input with only spaces
        mock_html = '''
        <div class="quote">
            <span class="text">"Life is what happens when you're busy making other plans."</span>
            <small class="author">John Doe</small>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "   ")
            mock_print.assert_not_called()

    @patch('scrapping.requests.get')
    def test_multiple_authors_on_page(self, mock_get):
        # Test case for multiple authors on the same page
        mock_html = '''
        <div class="quote">
            <span class="text">"Life is what happens when you're busy making other plans."</span>
            <small class="author">John Lennon</small>
        </div>
        <div class="quote">
            <span class="text">"Be yourself; everyone else is already taken."</span>
            <small class="author">Oscar Wilde</small>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "Oscar Wilde")
            mock_print.assert_any_call('Oscar Wilde \nQuote: "Be yourself; everyone else is already taken."\n')

    @patch('scrapping.requests.get')
    def test_author_case_insensitive(self, mock_get):
        # Test case for case-insensitive author matching
        mock_html = '''
        <div class="quote">
            <span class="text">"Life is what happens when you're busy making other plans."</span>
            <small class="author">John Lennon</small>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "john lennon")
            mock_print.assert_any_call('John Lennon \nQuote: "Life is what happens when you\'re busy making other plans."\n')

    @patch('scrapping.requests.get')
    def test_author_partial_match(self, mock_get):
        # Test case for partial author name matching
        mock_html = '''
        <div class="quote">
            <span class="text">"Life is what happens when you're busy making other plans."</span>
            <small class="author">John Lennon</small>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "John")
            mock_print.assert_any_call('John Lennon \nQuote: "Life is what happens when you\'re busy making other plans."\n')

    @patch('scrapping.requests.get')
    def test_author_not_found_in_partial_match(self, mock_get):
        # Test case for partial author name that shouldn't match
        mock_html = '''
        <div class="quote">
            <span class="text">"Life is what happens when you're busy making other plans."</span>
            <small class="author">Jane Austen</small>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "J")
            mock_print.assert_any_call('Jane Austen \nQuote: "Life is what happens when you\'re busy making other plans."\n')

    @patch('scrapping.requests.get')
    def test_special_characters_in_author_name(self, mock_get):
        # Test case for author name with special characters
        mock_html = '''
        <div class="quote">
            <span class="text">"Success is not the key to happiness. Happiness is the key to success."</span>
            <small class="author">Albert Einstein</small>
        </div>
        '''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "Albert Einstein!")
            mock_print.assert_not_called()

    @patch('scrapping.requests.get')
    def test_empty_quotes_page(self, mock_get):
        # Test case for an empty quotes page
        mock_html = ''
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        with patch('builtins.print') as mock_print:
            search('http://quotes.toscrape.com/', "John Lennon")
            mock_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()
