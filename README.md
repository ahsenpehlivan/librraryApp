# Library Management CLI

![Python](https://img.shields.io/badge/Python-CLI-3776AB?logo=python&logoColor=white)

A small, menu-driven library application written in Python. It keeps book and student records in local text files and supports a simple checkout workflow.

## Features

- List all books or only checked-out books
- Add and delete books
- Search by ISBN or book name
- Check out a book to a student and list students

## Run locally

From the repository root:

```bash
python libraryapp.py
```

The program reads and writes `bookfile.txt` and `studentfile.txt` in the current directory. Run it from the repository root so those files are found.

## Project scope

This is a console-based learning project with local file storage. It has no server, database, or multi-user access.
