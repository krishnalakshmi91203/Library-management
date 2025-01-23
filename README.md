# E-Library Management System

This project is an **E-Library Management System** designed to manage e-books and facilitate transactions between general users and librarians. It includes robust user authentication, role-based functionalities, and an intuitive interface for managing sections, books, and transactions.

---

## Features Overview

### 1. **Sections**
- **Description**: Stores information about different sections/categories of e-books.
- **Fields**:
  - `ID`: Unique identifier for the section.
  - `Name`: Name of the section.
  - `Creation Date`: Date when the section was created.
  - `Description`: Description of the section.

### 2. **Books**
- **Description**: Contains details about individual e-books, including content, authorship, and section association.
- **Fields**:
  - `ID`: Unique identifier for the book.
  - `Name`: Title of the e-book.
  - `Content`: Content of the e-book.
  - `Author`: Author of the e-book.
  - `SectionID`: Foreign key referencing the `Section` table.
  - `Price`: Price of the e-book.
  - `Rating`: Rating of the e-book.

### 3. **Users**
- **Description**: Stores user information, including role, login credentials, and contact details.
- **Fields**:
  - `Name`: Full name of the user.
  - `Role`: User's role (e.g., general user or librarian).
  - `uname`: Unique username.
  - `Pwd`: Hashed password for secure authentication.
  - `Number`: Contact number.
  - `Email`: Email address.

### 4. **Transactions**
- **Description**: Manages the transactions between users and e-books, tracking issued books, return dates, and transaction statuses.
- **Fields**:
  - `SectionID`: Foreign key referencing the `Book` table.
  - `BookID`: Foreign key referencing the `Book` table.
  - `Username`: Foreign key referencing the `User` table.
  - `Date Issued`: Date when the e-book was issued.
  - `Return Date`: Expected return date for the e-book.
  - `Status`: Current status of the transaction.

---

## User Authentication
The system incorporates a robust user authentication mechanism. Both general users and librarians are required to provide a username and password for secure access.

---

## Functionalities

### General Users
- **Features**:
  - Login/Register functionality.
  - Browse existing sections and e-books.
  - Request and return e-books.
  - Provide feedback on e-books.
- **Constraints**:
  - Users can request up to 5 e-books.
  - Access is automatically revoked after 7 days.

### Librarians
- **Features**:
  - Manage sections and books (add/edit/delete entries).
  - Issue or revoke access to e-books.
  - Monitor transaction statuses.
  - Access a dedicated dashboard for efficient system operations.

---

## Search Functionality
The system includes a robust search feature, allowing users to efficiently discover e-books based on various criteria such as:
- Section
- Author
- Title

---

## Technologies Used
- **Frontend**: HTML ,Bootstrap
- **Backend**: Flask , Jinja2
- **Database**: SQLite
---

## How to Run
1. Clone the repository.
2. Set up the database by running the migration scripts.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Start the Flask server: `python app.py`.


---


