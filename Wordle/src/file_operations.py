# import json

# def json(file_path):
#     """
#     Loads words from a text(txt)file.

#     parameters: file_path: Path to txt file
#     return: list of words
#     """
#     try:
#         with open(file_path, 'r') as file:
#             words = json.load(file)
#         return words
#     except FileNotFoundError:
#         print(f"Error: The file{file_path} does not exist.")
#     except Exception as e:
#         print(f"An unexpected error occured: {e}")
#         return []

# def move_word(file_path, words):
#     try:
#         with open(file_path, 'w') as file:
#             json.dump(words, file, indent=4)
#         print(f"Word sucessfully moved to {file_path}.")
#     except PermissionError:
#         print("f Error: Permission denied to write")
#     except Exception as e:
#         print("An unexpected error occured", e)