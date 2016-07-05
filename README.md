# POS-System
[![License][license-svg]][license-url]
[![Status][status-svg]][status-url]

A simple Point-of-Sale system with graphic interface. The system is controlled by one person at time.

<br>
#### Design
The system is developed in python snd designed with [tkinter][tkinter]!. 

#### How it works
All the workers are registered on the system, and when someone start to work, needs to login in is account and logout at the end.
Everything will keep registered.
The system load from a database what is still available and what's not available. When someting's stock is almost ending, the user will be warned.
The administrator will take care of the available itens.

#### Storing data
The choosen database was [MongoDB][tkinter]!.


[license-svg]: https://img.shields.io/badge/license-GNU%20v.3-blue.svg
[license-url]: https://github.com/iamthekyt/POS-System
[status-svg]: https://img.shields.io/pypi/status/Django.svg?maxAge=2592000
[status-url]: https://github.com/iamthekyt/POS-System
[tkinter]: <https://github.com/python/cpython/tree/master/Lib/tkinter>
[mongodb]: <https://docs.mongodb.com/getting-started/python/>
