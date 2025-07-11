import spam
from spam import Role

# = = = = = = = = =
# = = testing = = =
# = = = = = = = = =
namegen = iter(('alice', 'bob', 'carol', 'dave', 'edgar', 'francis', 'gerald', 'harry',
                'isabelle', 'jeffery', 'karl', 'liam', 'mary'))

class FakePerson:
    def __init__(self):
        self.uid = spam.random_string(50)
        self.name = next(namegen)

        spam.names[self.uid] = self.name

    def join(self, r):
        spam.names[self.uid] = self.name
        r.assignments.setdefault(self.uid)

# - - - - - - - - -
SL_FORM = {'num_players':6, 'num_lancelots':0,
                Role.merlin:True, Role.percival:False, Role.lover:False, Role.assassin:False, Role.morgana:True, Role.mordred:True, Role.oberon: False, Role.owain:False, Role.guardian_angel: True,
        }

# --- build sample room ----
backup = spam.session
spam.session = {'uid': 'tester'}
spam.names['tester'] = 'tester'
r = spam.Room('tester')
r.configure(spam.Configuration(SL_FORM))
spam.rooms['test'] = r
for _ in range(5):
    FakePerson().join(r)
spam.session = backup

r.possibly_make_assignments()

# --- already logged in
spam.names['bRrHUmsqwkMyfBcuizpbGDasIOSDgoIWQDUWvBVVhnMJyoJDvl'] = 'Chrome'
spam.names['BVRTPwTOfXKsoGSWgpwbSNwjeMXoQklPBpghHpBdfcPIlMJYzK'] = 'Firefox'

spam.app.run(debug=True)
