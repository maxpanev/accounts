class User:
    def __init__(self, id, username):
        self._id = id
        self._username = username
        self._access = "user"

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

    def get_access(self):
        return self._access


class Admin(User):
    def __init__(self, id, username, role):
        super().__init__(id, username)
        self._access = "admin"
        self.__role = role
        self._users = []

    def get_access(self):
        return self._access

    # Методы для доступа к role
    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def add_user(self, user):
        self._users.append(user)
        print(f"{self.get_username()} добавил пользователя - {user.get_username()}\n")

    def remove_user(self, user):
        self._users.remove(user)
        print(f"{self.get_username()} удалил пользователя - {user.get_username()}\n")

    def show_users(self):
        print(f"Список пользователей в системе:")
        print(f"ID: {self.get_id()}, Имя: {self.get_username()}, Уровень доступа: {self.get_access()}, Роль: {self.get_role()}")
        for u in self._users:
            print(f"ID: {u.get_id()}, Имя: {u.get_username()}, Уровень доступа: {u.get_access()}")
        print()


user1 = User(12345678, "Max")
user2 = Admin(87654321, "Nick", "Администратор системы")
user3 = User(12348765, "Mark")

user2.show_users()
user2.add_user(user1)
user2.add_user(user3)
user2.show_users()
user2.remove_user(user1)
user3.set_username("Andrew")
user2.set_role("Менеджер")
user2.show_users()