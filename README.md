# Dependency Graph

## Overview

Dependency Graph is a terminal-based Python application that helps visualize module dependencies in a project.

It allows you to:

- Add modules
- Define dependencies
- View dependency graphs
- Delete modules
- Store all data automatically

---

## Features

- Add Unlimited Modules
- Add Multiple Dependencies
- View Dependency Tree
- Delete Modules
- Automatic JSON Storage
- Simple Terminal Interface

---

## Project Structure

dependency-graph/

├── graph_engine.py

├── app.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

```bash
python app.py
```

---

## Example

### Add Module

```
Module Name:

Authentication
```

Dependencies

```
Database

JWT

Email

done
```

---

### View Graph

```
Authentication

└── Database

└── JWT

└── Email
```

---

### Another Example

```
Orders

└── Authentication

└── Database

└── Payments
```

---

## Generated File

```
dependencies.json
```

Example

```json
{
    "Authentication": [
        "Database",
        "JWT",
        "Email"
    ],
    "Orders": [
        "Authentication",
        "Database",
        "Payments"
    ]
}
```

---

## Future Improvements

- Nested Dependency Tree
- Circular Dependency Detection
- Export Graph to JSON
- Graph Visualization
- Search Module
- Rename Module
- Dependency Validation
- Import Existing Graph

---

## License

MIT License