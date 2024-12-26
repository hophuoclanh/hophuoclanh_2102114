class LoginSystem:
    def __init__(self):
        self.users = {}
        self.logged_users = set()
        self.mapping = {
            "a": "i", "b": "l", "c": "q", "d": "f", "e": "z", "f": "s",
            "g": "a", "h": "g", "i": "e", "j": "p", "k": "w", "l": "o",
            "m": "v", "n": "u", "o": "b", "p": "j", "q": "k", "r": "n",
            "s": "x", "t": "d", "u": "h", "v": "y", "w": "t", "x": "m",
            "y": "r", "z": "c"
        }

    def encrypt(self, password):
        return "".join(self.mapping[char] for char in password if char in self.mapping)

    def register(self, username, password):
        if username in self.users:
            print("user already exists")
        else:
            encrypted_password = self.encrypt(password)
            self.users[username] = encrypted_password
            print("user registered successfully")

    def login(self, username, password):
        if username not in self.users:
            print("user isn't in the system")
        else:
            encrypted_password = self.encrypt(password)
            if self.users[username] != encrypted_password:
                print("password doesn't match")
            else:
                self.logged_users.add(username)
                print("user logged in successfully")

    def sign_out(self, username):
        if username not in self.users:
            print("user is not in the system")
        elif username not in self.logged_users:
            print("user is not logged in")
        else:
            self.logged_users.remove(username)
            print("user signed out successfully")
        