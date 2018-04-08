import random, datetime
random.seed(datetime.datetime.now())

#
# DATA
#

BIG_NUMBERS = [
	"6 trillion",
	"3.4 million",
	"over 80,000",
	"18,003",
	"Graham's Number",
	"a googol",
	"a mole"
]

SMALL_NUMBERS = [
	"8",
	"sixteen",
	"42 and a half",
	"5",
	"43"
]

TINY_NUMBERS = [
	"one",
	"2",
	"three-quarters",
	"four eighteenths",
	"0.87"
]

NUMBERS = BIG_NUMBERS + SMALL_NUMBERS + TINY_NUMBERS

STAR_WARS_CHARACTERS = [
	"Darth Jar-Jar",
	"Nien Nunb",
	"an extra",
	"Ference the Rebel",
	"Clone Trooper ID# 86753099"
]

WORLD_LEADERS = [
	"Barack Obama",
	"Mao Zedong",
	"Moon Jae-In",
	"Bennito Musselini",
	"Nicolas Maduro",
	"Sam Houston",
	"Emperor Norton I",
	"Angela Merkel",
	"Xi Jin-Ping",
	"Vladimir Putin",
	"Donald Trump",
	"Macron",
	"Kim Jong-Un",
	"Kim Jong-Il",
	"Jeremy",
	"Justin Trudeau",
	"Henrique Peña Nieto",
]

PEOPLE = [
	"Eddie Vedder",
	"Ta-Nehisi Coates",
	"Honey Boo-Boo",
	"Masahiro Sakurai",
	"Shigeru Miyamoto",
	"Sam Ferraro",
	"the creator of Lindor chocolates",
	"your neighborhood gardener",
	"the Ghost of Christmas Past",
	"Peter Gabriel",
	"Elon Musk",
	"David Bowie",
	"Billy Joel's second wife",
	"my dentist",
	"Carl",
	"that kid from third grade",
	"that guy, you know the one --",
	"your mother",
	"Amanuel"
] + STAR_WARS_CHARACTERS + WORLD_LEADERS

COUNTRIES = [
	"China",
	"America",
	"Sudan",
	"what's left of Syria",
	"Suriname",
	"the country formally known as Hawaii",
	"Neo Hawaii",
	"Canada",
	"Brazil",
	"Equador",
	"Uruguay",
	"Tanzania",
	"Malaysia",
	"Isle of Mann",
	"Iceland",
	"Sandwich Islands",
	"Montserrat",
	"the U.K.",
	"Djibouti",
	"Italy",
	"Croatia",
	"South Africa",
	"Lesotho",
	"Japan",
	"Australia",
	"Papua New Guinea"
]

CITIES = [
	"Albequerque",
	"Baltimore",
	"Boring",
	"Washington D.C.",
	"Bishop's Head",
	"Accident",
	"Taylor's Island",
	"Paris, Texas",
	"Paris",
	"Paris, France",
	"Earth, Texas",
	"Atlanta",
	"Tulsa"
]

PLACES = [
	"your bedroom",
	"the inn",
	"Yas Island",
	"your local Dunkin Donuts",
	"Fantasylandia",
	"the place that Ferraro comes from",
	"the place down the street",
	"the place next door",
	"the site of the Titanic",
	"there"
] + CITIES

OBSCURE_ANIMALS = [
	"Pink Fairy Armadillo",
	"Griffin",
	"Chimaera",
	"Tardigrade",
	"Trilobyte",
	"White Rhino",
	"Quagga",
	"Axolotl",
	"Wallaby",
	"Echidna",
]

ANIMALS = [
	"deer",
	"bear",
	"wolf",
	"goldfish",
	"your pet dog",
	"aardvark",
	"dwarf",
	"panda",
	"human",
	"tiger",
	"eagle",
	"lion",
	"toad",
	"lizard",
	"bearded dragon",
	"hamster",
	"cat",
	"gerbil",
	"iguana",
	"goose",
	"duck",
	"pig",
	"cow",
	"Cow",
	"cattle",
	"yellow bellied swallow",
	"gorile",
	"gorilla",
	"your neighbor",
	"koala"
] + OBSCURE_ANIMALS

DISEASES = [
	"Ebola",
	"Malaria",
	"Mad Cow Disease",
	"Common Cold",
	"the Flu",
	"strep throat",
	"Tuberculosis",
	"Cancer",
	"smallpox"
]

HOBBIES = [
	"bowling",
	"fishing",
	"programming small universe-destroying nanobots",
	"recreating entire episodes of Phineas and Ferb frame-by-frame in live action",
	"drumming",
	"fly-fishing",
	"shoemaking",
	"creating panic in subreddits",
	"marathoning Shrek",
	"barking at doors",
	"crab-walking across the USA",
	"crying themselves to sleep",
	"breaking Nicholas",
	"spending your significant other's life savings"
]

MATERIALS = [
	"wood",
	"bone",
	"glass",
	"human flesh",
	"fabric",
	"flourescent toothpaste",
	"carbon nanotubes",
	"Vantablack",
	"invisible scum",
	"chemically rearranged ivory"
]

IDEAS = [
	"We should put Pluto in a tractor beam so we can be better friends!",
	"How much are the Chicken McNuggets?",
	"Why not?",
	"PS/2 is the superior keyboard interface!",
	"You're wrong because of that.",
	"Wait, which way was the bank? My map happened to spontaneously vaporize.",
	"Dang it.",
	"I'm a dwarf!"
]

MAP = {
	"bn" : BIG_NUMBERS,
	"sn" : SMALL_NUMBERS,
	"tn" : TINY_NUMBERS,
	"n" : NUMBERS,
	"wl" : WORLD_LEADERS,
	"p" : PEOPLE,
	"swc" : STAR_WARS_CHARACTERS,
	"cn" : COUNTRIES,
	"ct" : CITIES,
	"pl" : PLACES,
	"oa" : OBSCURE_ANIMALS,
	"a" : ANIMALS,
	"ds" : DISEASES,
	"hb" : HOBBIES,
	"mat" : MATERIALS,
	"idea" : IDEAS,
}

QUESTIONS = [
	"The Native Americans were here for [bn] years before us!",
	"The average tree is [sn] meters tall.",
	#"Nicholas is named Gus.",
	"The average digeridoo is supposed to played by [sn] people at once.",
	"In the newest STAR WARS movie, [swc] kills [swc] in the climactic scene towards the end of the movie!",
	"[p] once ate a healthy meal in [pl].",
	"There is a one in a [bn] chance to see a flying [oa] in your lifetime. Good Luck!",
	"There is a one in a [bn] chance each year that an [a] forces a [oa] out of their natural habitat.",
	"[n] [a]s are forced out of their natural habitat each year.",
	"George Lucas recently had the idea to digitally replace [swc] with [p] in STAR WARS: Episode IV.",
	"[wl] implied in an interview that [ct] would be an ideal nuclear target. Residents agree.",
	"[wl] has a [tn] percent chance to spontaneously combust in the next [sn] days.",
	"In a recent behind-the-scenes interview, George Lucas revealed that [swc] is based off of [p]!",
	"Newest census reveals that in [ct] only [tn] percent of the population are permanent residents!",
	"After [wl] snapped at [wl], in both [ct] and [ct] tensions have been high. War has been discussed.",
	"[tn] percent of scientists, including [p] are working on curing [ds] each year. They haven't done anything yet.",
	"Recently, a movement has gained traction for [pl] to secede from the European Union.",
	"The oldest [oa] is [tn] years old.",
	"Recently, [wl] has taken up [hb].",
	"The national sport of [cn] is [hb].",
	"Each year, more and more people consider [hb] over talking to their parents.",
	"[hb] has recently been recognized as an Olympic sport. It is reported that [p] will participate.",
	"Did you know? There is a church in [cn] made out of [mat]!",
	"BREAKING NEWS: The chance that there is [mat] on Mars has raised by [sn] percent, according to probe. Scientists scrambling to find answers.",
	"Word's been going around town that [wl] is having an affair with [p]. They're trying to keep it hushed up.",
	"[ct] has recently been found to be sitting on top of a [mat] mine! In fact, [cn] is supposed to be full of it.",
	"The latest film, \"[p] and [p] in [cn]: Can they Escape?\" has received adverse reviews from fans. Critics aren't sure what to think.",
	"By the time the next solar eclipse happens, the [a] species is expected to have gone extinct.",
	"[p] was found writing graffiti on a billboard in [ct]. His graffiti read, \"[idea]\" People aren't sure whether to remove it, as it seems like it could be a valuable addition to the area."
]

#
# PROCESSING
#

for i in range(20):
	question = random.choice(QUESTIONS)

	for key in MAP:
		actualKey = "[" + key + "]"

		while actualKey in question:
			item = random.choice(MAP[key])

			question = question.replace(actualKey, item, 1)

	question = question[0].upper() + question[1:]

	print(question)
