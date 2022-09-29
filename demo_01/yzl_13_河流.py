river_dict = {"nile": "egypt",
              "changjiang": "china",
              "amu": "uzbekistan"
              }
for river in river_dict.keys():
    print(river)

for country in river_dict.values():
    print(country)

# for rivers in river_dict.keys():
#
#     print(f"The {rivers.title()} runs through {river_dict[rivers]}")

for rivers, countrys in river_dict.items():
    print(f"The {rivers.title()} runs through {countrys.title()}")