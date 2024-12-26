### Simple Register Login System

#### Overview
The `LoginSystem` class implements a simple user authentication system. It provides methods for user registration, login, and logout. User passwords are encrypted before storage using a predefined character mapping for added security.

---

#### Class: `LoginSystem`

##### Attributes:
1. **`users`**
   - **Type**: `dict`
   - **Description**: Stores registered users and their encrypted passwords. Keys are usernames, and values are encrypted passwords.

2. **`logged_users`**
   - **Type**: `set`
   - **Description**: Tracks the usernames of currently logged-in users.

3. **`mapping`**
   - **Type**: `dict`
   - **Description**: Defines the character-to-character mapping for password encryption.

---

#### Methods:

1. **`__init__(self)`**
   - **Description**: Initializes the `LoginSystem` with empty user data and a predefined encryption mapping.

2. **`encrypt(self, password)`**
   - **Description**: Encrypts a password using the predefined `mapping`.
   - **Parameters**:
     - `password` (str): The plaintext password to be encrypted.
   - **Returns**:
     - (str): The encrypted password.

3. **`register(self, username, password)`**
   - **Description**: Registers a new user with their username and encrypted password.
   - **Parameters**:
     - `username` (str): The username for the new user.
     - `password` (str): The plaintext password for the new user.
   - **Behavior**:
     - If the username already exists, prints "user already exists."
     - Otherwise, encrypts the password, stores it, and prints "user registered successfully."

4. **`login(self, username, password)`**
   - **Description**: Logs in a user after verifying their credentials.
   - **Parameters**:
     - `username` (str): The username of the user.
     - `password` (str): The plaintext password entered by the user.
   - **Behavior**:
     - If the username does not exist, prints "user isn't in the system."
     - If the encrypted password does not match the stored password, prints "password doesn't match."
     - If both checks pass, adds the username to `logged_users` and prints "user logged in successfully."

5. **`sign_out(self, username)`**
   - **Description**: Logs out a user.
   - **Parameters**:
     - `username` (str): The username of the user to be logged out.
   - **Behavior**:
     - If the username does not exist, prints "user is not in the system."
     - If the user is not logged in, prints "user is not logged in."
     - Otherwise, removes the username from `logged_users` and prints "user signed out successfully."

---

#### Notes:
- Password encryption is for demonstration purposes only and is not secure for real-world applications.
- Only lowercase alphabetical characters are supported for password encryption. Other characters are ignored.
- The system assumes users will always input valid lowercase passwords during registration and login.