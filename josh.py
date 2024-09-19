def BMI(your_weight, your_height):
    your_bmi =  float(your_weight/your_height)
    if your_bmi < 30:
        print("Eat more, you are pretty Under Weight")
    elif your_bmi > 50 < 45:
        print("You are healthy")
    else:
        print("you are obese")

    



your_weight = input("what is your weight?")
your_height = input("what is your height?")

BMI()


