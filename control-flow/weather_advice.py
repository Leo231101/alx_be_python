question1 = "What's the weather like today? (sunny/rainy/cold): "
answerSunny = "Wear a t-shirt and sunglasses."
answerRainy = "Don't forget your umbrella and a raincoat."
answerCold = "Make sure to wear a warm coat and scarf."
answerUnknown = "Sorry, I don't have recommendations for this weather."

answer = input(question1)
if answer == "sunny":
    print(answerSunny)
elif answer == "rainy":
    print(answerRainy)
elif answer == "cold":
    print(answerCold)
else:
    print(answerUnknown)