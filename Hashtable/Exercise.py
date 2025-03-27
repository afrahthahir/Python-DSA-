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

# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan

# What was the temperature on Jan 9?
# What was the temperature on Jan 4?

temperatureJan9 = nycWeather.get("Jan 9")
print("temperature on Jan 9",temperatureJan9)

temperatureJan4 = nycWeather.get("Jan 4")
print("temperature on Jan 4",temperatureJan4)




weather = [27,31,23,34,37,38,29,30,35,30]
average = sum(weather[0:7]) / len(weather[0:7])
maxTemp = max(weather)
#Using list data structure here because it is the best one to use for this scenario
print("average temperature in first week of Jan", average)
print("maximum temperature in first 10 days of Jan", maxTemp)

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