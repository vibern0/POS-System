# POS-System

A simple Point-of-Sale system with graphic interface. The system is controlled by one person at time.

## Installation

Make sure to have [kivy](https://kivy.org/doc/stable/installation/installation.html) installed. Follow the link to do so.

This application uses an *sqlite* database, which by default is on the same folder as the source code. You can create a new database and run the [schema.sql](src/schema.sql) and then add some dummy data like 

```sql
INSERT INTO products (name, type, stock, price) VALUES ('Product XYZ','meat',5,30);
INSERT INTO users (name,password) VALUES ('admin1','admin1');
```

## Usage

```bash
python main.py
```

#### How it works

All the workers are registered on the system, and when someone starts to work, needs to login in his account and logout at the end.
Everything keeps registered.
The system loads from a database what is still available and what's not available. When something  in the stock is almost ending, the user will be warned.
The administrator will take care of the available items.

#### Manage accounts

The administrator as a panel to manage accounts in the system. Each employee has a card with a username and a password.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU v3](LICENSE.md)