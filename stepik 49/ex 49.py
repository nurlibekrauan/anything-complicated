# Вложенные классы | Объектно-ориентированное программирование Python
class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + psw)

    class Meta:
        ordering = ["id"]

        def __init__(self, access) -> None:
            self._access = access
            self._t = Women.title


# внутренный класс должен использоваться внешним классом (не наоборот)
w = Women("root", "12345")
print(w.ordering)
print(w.__dict__)
print(w.meta.__dict__)
