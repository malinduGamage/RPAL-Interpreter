class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def get_type(self):
        return self.type

    def get_value(self):
        return self.value

    def set_type(self, type_):
        self.type = type_

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return "<{}: {}>".format(self.type, self.value)

    def __repr__(self) :
        return f'{self.token} {self.pos} {self.lemma} {self.dep} {self.head} {self.ner}'

    def __eq__(self, other) :
        return self.token == other.token and self.pos == other.pos and self.lemma == other.lemma and self.dep == other.dep and self.head == other.head and self.ner == other.ner

    def __ne__(self, other) :
        return not self.__eq__(other)

    def __hash__(self) :
        return hash((self.token, self.pos, self.lemma, self.dep, self.head, self.ner))

    def __lt__(self, other) :
        return self.token < other.token

    def __le__(self, other) :
        return self.token <= other.token

    def __gt__(self, other) :
        return self.token > other.token

    def __ge__(self, other) :
        return self.token >= other.token

    def __len__(self) :
        return len(self.token)

    def __getitem__(self, key) :
        return self.token[key]

    def __iter__(self) :
        return iter(self.token)

    def __contains__(self, item) :
        return item in self.token

    def __add__(self, other) :
        return self.token + other

    def __radd__(self, other) :
        return other + self.token

    def __mul__(self, other) :
        return self.token * other

    def __rmul__(self, other) :
        return other * self.token

    def __iadd__(self, other) :
        self.token += other
        return self

    def __imul__(self, other) :
        self.token *= other
        return self

    def __isub__(self, other) :
        self.token -= other
