# Django-assignment
## Task:
Your task is to create a Django application that is a feeds reader. The app can read feed from multiple sources and store them to database.
## Requirements:
- [x] As a developer, I want to run a command which help me to setup database easily with one run.
- [x] As a developer, I want to run a command which accepts the feed urls (separated by comma) asargument to grab items from given urls.Duplicate items are accepted.
- [x] As a developer, I want to see output of the command not only in shell but also in pre-defined log file. The log file should be defined as a parameter of the application.
- [x] As a user, I want to see the list of items which were grabbed by running the command line above, via web-based. I also should see the pagination if there are more than one page. The page size is a configurable value.
- [x] As a user, I want to filter items by category name on list of items.
- [x] As a user, I want to create new item manually via a form.
- [x] As a user, I want to update/delete an item
## How to setup:
### Require of project
- python3 (>3.5)
- Dependences: please check [requirements](./requirements.txt)
### Models
- `Channel` is represent feed, which has a  `link`
- `Channel` have many `Item` contain the content.
### Setup database
- Using default database of django sqlite3.
- Database run:
`python manage.py makemigrations` for create model objects
`python manage.py migrate` run datebase
### Command to grab item
`python manage.py grab_item <list_of_urls_seperate_by_comma> <log_file>`
* <list_of_urls_seperate_by_comma>: List of feeds URLs need to grab item (seperate by comma)
* <log_file>: path of log file to store while grab item
### Run web based
- Dependences install `pip install -r requirements.txt`
- `cd assignment`
- Run server `python manage.py runserver`
- On the localhost `localhost:8000/assignment/`
### Web based interface
- List of grab channel: `<server_host>:<server_port>/assignment/`
- Detail of channel: `<server_host>:<server_port>/assignment/<channel_id>`
- Edit channel `<server_host>:<server_port>/assignment/edit_channel/<channel_id>`
- Display all item belong channel: `<server_host>:<server_port>/assingment/items/<channel_id>`
- Detail of item: `<server_host>:<server_port>/assignment/detail_item/<item_id>`
- Edit item: `<server_host>:<server_port>/assignment/edit_item/<item_id>`


