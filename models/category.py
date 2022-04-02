#!/usr/bin/python3

class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, cat_id):
        if not cat_id:
            raise ValueError('Category ID cannot be NULL')
        self._category_id = int(cat_id)

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, cat_name):
        if not cat_name:
            raise ValueError('Category name cannot be NULL')
        self._category_name = cat_name

if __name__ == '__main__':
    category = Category(1, 'Groceries')
    print(category.category_id)
    print(category.category_name)
