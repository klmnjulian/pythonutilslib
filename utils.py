# pythonutilslib
# File containing utility functions for common tasks.
# Copyright Julian Kalman (@klmnjulian) 2024

import random
import string
import re
import hashlib
import unicodedata
import math
import os
import json
import csv
from typing import List, Tuple, Union, Any


class Utils:
    @staticmethod
    def generate_random_password(length: int = 10) -> str:
        """
        Generates a random password of given length.

        Args:
            length (int): Length of the generated password. Default is 10.

        Returns:
            str: Randomly generated password.
        """
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    @staticmethod
    def camel_case_to_snake_case(text: str) -> str:
        """
        Converts a camelCase string to snake_case.

        Args:
            text (str): CamelCase string to convert.

        Returns:
            str: Converted snake_case string.
        """
        return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

    @staticmethod
    def snake_case_to_camel_case(text: str) -> str:
        """
        Converts a snake_case string to camelCase.

        Args:
            text (str): snake_case string to convert.

        Returns:
            str: Converted camelCase string.
        """
        parts = text.split('_')
        return parts[0] + ''.join(x.title() for x in parts[1:])

    @staticmethod
    def reverse_string(text: str) -> str:
        """
        Reverses a string.

        Args:
            text (str): String to reverse.

        Returns:
            str: Reversed string.
        """
        return text[::-1]

    @staticmethod
    def count_vowels(text: str) -> int:
        """
        Counts the number of vowels in a string.

        Args:
            text (str): Input string.

        Returns:
            int: Number of vowels in the string.
        """
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)

    @staticmethod
    def remove_duplicates(text: str) -> str:
        """
        Removes duplicate characters from a string.

        Args:
            text (str): Input string.

        Returns:
            str: String with duplicate characters removed.
        """
        return ''.join(sorted(set(text), key=text.index))

    @staticmethod
    def calculate_hash(text: str, algorithm: str = 'md5') -> str:
        """
        Calculates the hash of a string using the specified algorithm.

        Args:
            text (str): Input string.
            algorithm (str): Hash algorithm to use. Default is 'md5'.

        Returns:
            str: Hashed value of the input string.
        """
        hash_algorithm = hashlib.new(algorithm)
        hash_algorithm.update(text.encode('utf-8'))
        return hash_algorithm.hexdigest()

    @staticmethod
    def normalize_text(text: str) -> str:
        """
        Normalizes text by removing accents and converting to lowercase.

        Args:
            text (str): Input string.

        Returns:
            str: Normalized string.
        """
        return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower()

    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Checks if a number is prime.

        Args:
            number (int): Input number.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def generate_prime_numbers(limit: int) -> List[int]:
        """
        Generates prime numbers up to the given limit.

        Args:
            limit (int): Upper limit for generating prime numbers.

        Returns:
            List[int]: List of prime numbers.
        """
        primes = []
        for num in range(2, limit + 1):
            if Utils.is_prime(num):
                primes.append(num)
        return primes

    @staticmethod
    def factorial(number: int) -> int:
        """
        Calculates the factorial of a number.

        Args:
            number (int): Input number.

        Returns:
            int: Factorial of the input number.
        """
        if number == 0:
            return 1
        return number * Utils.factorial(number - 1)

    @staticmethod
    def is_palindrome(text: str) -> bool:
        """
        Checks if a string is a palindrome.

        Args:
            text (str): Input string.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        return text == text[::-1]

    @staticmethod
    def list_intersection(list1: List[Any], list2: List[Any]) -> List[Any]:
        """
        Finds the intersection of two lists.

        Args:
            list1 (List[Any]): First input list.
            list2 (List[Any]): Second input list.

        Returns:
            List[Any]: Intersection of the two input lists.
        """
        return list(set(list1) & set(list2))

    @staticmethod
    def list_union(list1: List[Any], list2: List[Any]) -> List[Any]:
        """
        Finds the union of two lists.

        Args:
            list1 (List[Any]): First input list.
            list2 (List[Any]): Second input list.

        Returns:
            List[Any]: Union of the two input lists.
        """
        return list(set(list1) | set(list2))

    @staticmethod
    def list_difference(list1: List[Any], list2: List[Any]) -> List[Any]:
        """
        Finds the difference of two lists.

        Args:
            list1 (List[Any]): First input list.
            list2 (List[Any]): Second input list.

        Returns:
            List[Any]: Difference of the two input lists.
        """
        return list(set(list1) - set(list2))

    @staticmethod
    def save_json(data: Union[dict, list], filename: str) -> None:
        """
        Saves data to a JSON file.

        Args:
            data (Union[dict, list]): Data to be saved.
            filename (str): File path to save the data.
        """
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_json(filename: str) -> Union[dict, list]:
        """
        Loads data from a JSON file.

        Args:
            filename (str): File path to load the data.

        Returns:
            Union[dict, list]: Loaded data from the JSON file.
        """
        with open(filename, 'r') as f:
            return json.load(f)

    @staticmethod
    def save_csv(data: List[List[Any]], filename: str, headers: List[str] = None) -> None:
        """
        Saves data to a CSV file.

        Args:
            data (List[List[Any]]): Data to be saved.
            filename (str): File path to save the data.
            headers (List[str], optional): List of headers for the CSV file. Defaults to None.
        """
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            if headers:
                writer.writerow(headers)
            writer.writerows(data)

    @staticmethod
    def load_csv(filename: str) -> List[List[str]]:
        """
        Loads data from a CSV file.

        Args:
            filename (str): File path to load the data.

        Returns:
            List[List[str]]: Loaded data from the CSV file.
        """
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            return [row for row in reader]

    @staticmethod
    def create_directory(directory: str) -> None:
        """
        Creates a directory if it doesn't exist.

        Args:
            directory (str): Directory path to create.
        """
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """
        Calculates the distance between two points in 2D space.

        Args:
            point1 (Tuple[float, float]): Coordinates of the first point (x1, y1).
            point2 (Tuple[float, float]): Coordinates of the second point (x2, y2).

        Returns:
            float: Euclidean distance between the two points.
        """
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Add more utility functions here...

if __name__ == "__main__":
    text = "HelloWorld"
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    point1 = (1, 2)
    point2 = (4, 6)
    
    print("Random Password:", Utils.generate_random_password())
    print("Camel Case to Snake Case:", Utils.camel_case_to_snake_case(text))
    print("Reversed String:", Utils.reverse_string(text))
    print("Number of Vowels:", Utils.count_vowels(text))
    print("Remove Duplicates:", Utils.remove_duplicates(text))
    print("MD5 Hash:", Utils.calculate_hash(text))
    print("Normalized Text:", Utils.normalize_text("l'école"))
    print("Is Prime:", Utils.is_prime(17))
    print("Prime Numbers:", Utils.generate_prime_numbers(20))
    print("Factorial:", Utils.factorial(5))
    print("Is Palindrome:", Utils.is_palindrome("madam"))
    print("List Intersection:", Utils.list_intersection(list1, list2))
    print("List Union:", Utils.list_union(list1, list2))
    print("List Difference:", Utils.list_difference(list1, list2))
    print("Distance between Points:", Utils.calculate_distance(point1, point2))
