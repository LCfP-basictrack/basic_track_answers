linkin_park_members = [  # "Chester Bennington", RIP
                         # "Mark Wakefield",
                       "Mike Shinoda",
                       "Dave \"Phoenix\" Farrell",
                       "Brad Delson",
                       "Joe Hahn",
                       "Rob Bourdon"]
linkin_park_roles = [  # "vocals",
                       # "vocals",
                     "vocals, rapping, rhythm guitar, keyboard, samples, synthesizer",
                     "bass, backing vocals",
                     "lead guitar, backing vocals",
                     "turntables, samples, programming, backing vocals",
                     "drums, percussion, occasional backing vocals"]

print("Introducing:")
for member, role in zip(linkin_park_members, linkin_park_roles):
    print("\t{} on {}".format(member, role))
