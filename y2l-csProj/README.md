# HackMEET: Y2 CS Summer Starter Kit
This is the starter kit for the websites for the Y2 Summer 2018.

## Instructions:
To use this starter kit: **DO NOT FORK!**
```bash
git clone https://github.com/meet-projects/y2s18-YOUR_TEAM_NUMBER-final.git
```
Make sure your clone link includes **YOUR ACTUAL TEAM NUMBER** instead of the placeholder **`YOUR_TEAM_NUMBER`**.

## File descriptions:

### `app.py`:
`app.py` contains all your Flask logic for app **routing and backend processing**.

### `databases.py`:
`databases.py` contains the database related functions (like adding items, querying, deleting, etc.). This is done for a more organized code.

### `model.py`:
`model.py` contains the schema, also known as **table structure**, of your database. You should define all the tables that you will need to use in your web app in this file. For example, you might create a `User` table here.

### `print_databases.py`:
`print_databases.py` is a helpful file that can display the items in your database for easier debugging! Example usage: ```python print_databases.py project.db```Test
