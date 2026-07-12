from countryinfo import CountryInfo

x= input("Enter country name: ")

country = CountryInfo(x)

print("Official Capital :", country.capital())
print("Currencies Used:", country.currencies())
print("Languages Used   :", country.languages())
print("Bordering Codes  :", country.borders())
print("Population Size  :", country.population())
