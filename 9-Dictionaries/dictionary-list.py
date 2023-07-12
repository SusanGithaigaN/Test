travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    
   new_country = {
       "country" : country,
       "visits" : visits,
       "cities" : cities
   }
   travel_log.append(new_country)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



# NESTING LISTS AND DICTIONARIES
# each key can only have one value
travels = [{
    "state": "France",
    "cities": ["Paris", "Morocco","Lille", "Dijion", "Kiambu"],
},
{
    "state": "Kenya",
    "cities":{"towns": ["Just", "making", "random", "guesses"], "main_town": "Machakos"}
}]

def new_citie(state, cities):
    # capitals = {
    #     "France": "Paris",
    #     "Kenya": "Nairobi",
    #     "South Sudan": "Khaourtum"
    # }


    # Nesting a dictionary in a dictionary  
       citie = {
       "state" : state,
       "cities" : cities
   }
       travels.append(citie)
       
new_citie("Kenya", ["Diani", "Kwa Vonza", "Muguka"])       
print(travels)