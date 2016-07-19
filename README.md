# POS-System
[![License][license-svg]][license-url]
[![Status][status-svg]][status-url]

A simple Point-of-Sale system with graphic interface. The system is controlled by one person at time.

<br>
#### Design
The system is developed in python and designed with [Kivy][kivy]. 

#### How it works
All the workers are registered on the system, and when someone start to work, needs to login in is account and logout at the end. This registery system is based on key cards.
Everything keeps registered.
The system load from a database what is still available and what's not available. When someting's stock is almost ending, the user will be warned.
The administrator will take care of the available itens.

#### Storing data
The choosen database was [MongoDB][mongodb].

#### Manage accounts
The administrator as a panel to manage accounts in the system. The employers just need to pass the card in the machine detector and start his session.



[license-svg]: https://img.shields.io/badge/license-GNU%20v.3-blue.svg
[license-url]: https://github.com/iamthekyt/POS-System
[status-svg]: https://img.shields.io/pypi/status/Django.svg?maxAge=2592000
[status-url]: https://github.com/iamthekyt/POS-System
[kivy]: <https://github.com/kivy/kivy>
[mongodb]: <https://docs.mongodb.com/getting-started/python/>
