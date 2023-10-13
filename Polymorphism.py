"""poly   = many
   morphism=forms"""

class southkorea():
    def capital(self):
        print("korea is capital of india")

    def language(self):
        print("language is korean")


    def famous(self):
         print("india is famous of technology in the worlds ")

class india():
    def capital(self):
        print("New delhi is capital of india")

    def language(self):
        print("language is hindi")


    def famous(self):
         print("india is famous of democracy in the worlds ")





m=india()
t=southkorea()
for country in  (m,t):
    country.capital()
    country.language()
    country.famous()



