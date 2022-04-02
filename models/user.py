#!/usr/bin/python3

class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, u_id):
        if not u_id:
            raise ValueError('User ID cannot be NULL')
        self._user_id = int(u_id)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, f_name):
        if not f_name:
            raise ValueError('First name cannot be NULL')
        self._first_name = f_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, l_name):
        if not l_name:
            raise ValueError('Last name cannot be NULL')
        self._last_name = l_name

if __name__ == '__main__':
    user = User(1, 'Luke', 'Orth')
    print(user.user_id)
    print(user.first_name)
    print(user.last_name)
