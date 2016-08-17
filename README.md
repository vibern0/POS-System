# POS-System
[![License][license-svg]][license-url]
[![Status][status-svg]][status-url]

A simple Point-of-Sale system with graphic interface. The system is controlled by one person at time.

#### Design
The system is developed in python and designed with [Kivy][kivy]. 

#### How it works
All the workers are registered on the system, and when someone start to work, needs to login in his account and logout at the end.
Everything keeps registered.
The system load from a database what is still available and what's not available. When someting's stock is almost ending, the user will be warned.
The administrator will take care of the available itens.

#### Storing data
In this project, to save all data, a [SQLite3][sqlite3] local database is used. The database is already included in the project.

#### Manage accounts
The administrator as a panel to manage accounts in the system. Each employer have a card with a username and a password.



[license-svg]: https://img.shields.io/badge/license-GNU%20v.3-blue.svg
[license-url]: https://github.com/obernardovieira/POS-System
[status-svg]: https://img.shields.io/pypi/status/Django.svg?maxAge=2592000
[status-url]: https://github.com/obernardovieira/POS-System
[kivy]: <https://github.com/kivy/kivy>
[sqlite3]: https://docs.python.org/2/library/sqlite3.html
