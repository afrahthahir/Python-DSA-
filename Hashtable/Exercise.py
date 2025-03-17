nycWeather = {
    "Jan 1": 27,
    "Jan 2": 31,
    "Jan 3": 23,
    "Jan 4": 34,
    "Jan 5": 37,
    "Jan 6": 38,
    "Jan 7": 29,
    "Jan 8": 30,
    "Jan 9": 35,
    "Jan 10": 30
}

temperatureJan9 = nycWeather.get("Jan 9")
print(temperatureJan9)

temperatureJan4 = nycWeather.get("Jan 4")
print(temperatureJan4)

sum = 0
max = 0
for key, value in nycWeather.items():
    sum = sum + value
    if value > max:
        max = value

average = sum / len(nycWeather)
# print(len(nycWeather))
print(average)
print(max)

wordCount = {}

# opening the text file
with open('poem.txt','r') as file:
    # reading each line    
    for line in file:
        # reading each word        
        for word in line.split():
            
            if word in wordCount.keys():
                # print(word)
                occurence = wordCount[word] + 1
                wordCount[word] = occurence

            else:
                # print(word)
                wordCount[word] = 1
print(wordCount) 