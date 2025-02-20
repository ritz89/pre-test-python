import pytest
from main import validate_email, parse_user_data, get_title
from test import sum_numbers, reverse_string, find_max, is_palindrome, count_vowels

def test_sum_numbers():
    assert sum_numbers(1, 2) == 3
    assert sum_numbers(-5, 5) == 0
    assert sum_numbers(0, 0) == 0

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("Python") == "nohtyP"

def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-10, -20, -3]) == -3
    with pytest.raises(ValueError):
        find_max([])  # Fungsi harus raise ValueError pada list kosong

def test_is_palindrome():
    assert is_palindrome("radar") is True
    assert is_palindrome("hello") is False
    # Uji palindrome dengan perbedaan huruf besar dan kecil
    assert is_palindrome("Madam".lower()) is True

def test_count_vowels():
    assert count_vowels("hello") == 2  # huruf vokal: e, o
    assert count_vowels("world") == 1  # huruf vokal: o
    assert count_vowels("AEIOU") == 5
    assert count_vowels("") == 0

def test_validate_email():
    assert validate_email("user@example.com") == True
    assert validate_email("userexample.com") == False
    assert validate_email("user@com") == False
    assert validate_email("user@@example.com") == False

def test_parse_user_data_valid():
    json_str = '{"name": "John", "age": 30, "email": "john@example.com"}'
    data = parse_user_data(json_str)
    assert isinstance(data, dict)
    assert data.get("name") == "John"

def test_parse_user_data_invalid():
    # JSON tidak valid
    json_str = '{"name": "John", "age": 30, "email": "john@example.com"'
    data = parse_user_data(json_str)
    assert data == {}

def test_get_title():
    # Uji dengan URL yang sudah dikenal
    title = get_title("https://www.umkt.ac.id")
    assert "Universitas Muhammadiyah Kalimantan Timur" in title