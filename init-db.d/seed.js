print("Seed mongodb")
db.starwars.drop();
db.starwars.insertMany(
    [
  {
    "_id":"80884966-d276-4066-9f6c-718ce2ffc11e",
    "name": "Yavin IV",
    "climate": "temperate, tropical",
    "terrain": "jungle, rainforests"
  },
  {
    "_id": "5dda99a9-335a-4768-8ed7-0acb9f59944a",
    "name": "Tatooine",
    "climate": "arid",
    "terrain": "desert"
  },
  {
    "_id":"cf0aba97-da17-4e8c-bc58-8b5418cb7efa",
    "name": "Alderaan",
    "climate": "temperate",
    "terrain": "grasslands, mountains"
  },
  {
    "_id":"0ef42433-588a-4a09-94f5-11283ec473aa",
    "name": "Hoth",
    "climate": "frozen",
    "terrain": "tundra, ice caves, mountain ranges"
  },
  {
    "_id":"f7c02fe5-5aa5-4796-a951-6133fd04eb90",
    "name": "Dagobah",
    "climate": "murky",
    "terrain": "swamp, jungles"
  },
  {
    "_id":"fa719d9a-869a-4bdb-a448-e9616f573749",
    "name": "Bespin",
    "climate": "temperate",
    "terrain": "gas giant"
  },
  {
    "_id":"95f8e896-5458-4e32-b09e-402bdd44d742",
    "name": "Endor",
    "climate": "temperate",
    "terrain": "forests, mountains, lakes"
  },
  {
    "_id":"8dfcc6dd-202b-4f2a-a349-8842214a215c",
    "name": "Naboo",
    "climate": "temperate",
    "terrain": "grassy hills, swamps, forests, mountains"
  },
  {
    "_id":"509c70ec-bbb9-4aaf-bb1e-6d1bc2256452",
    "name": "Kamino",
    "climate": "temperate",
    "terrain": "ocean"
  },
  {
    "_id":"59c235b4-32ee-4121-b95a-85e81a852ce1",
    "name": "Geonosis",
    "climate": "temperate, arid",
    "terrain": "rock, desert, mountain, barren"
  },
  {
  "_id":"95f8e896-5458-4e32-b09e-402bdd44d742",
  "name": "Coruscant",
  "climate": "temperate",
  "terrain": "cityscape, mountains"
  }
]
)