from simple_register_login_system import LoginSystem

login_system = LoginSystem()

# Register users
inputs_register = [
    ("usera", "passa"),
    ("userb", "passb"),
    ("userc", "passc"),
    ("userc", "passc"),
    ("userd", "passd")
]

for username, password in inputs_register:
    login_system.register(username, password)

# Login users
inputs_login = [
    ("usera", "usera"),  # Incorrect password
    ("usera", "passa"),  # Correct password
    ("usera", "passa")   # Already logged in
]

for username, password in inputs_login:
    login_system.login(username, password)
