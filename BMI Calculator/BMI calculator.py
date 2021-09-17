#IBM healthy weight calculator

weight = input ('Enter your weight (in kg):')
height = input ('Enter your height (in m):')

weight_pound = float(weight) * 2.2
height_inches = float (height) * 39.37

healthy_weight = weight_pound/(pow(height_inches,2)) * 703

if healthy_weight < 18.5:
    print ('Underweight')
elif healthy_weight >= 18.5 and healthy_weight < 25:
    print ('Healthy')
elif healthy_weight >= 25 and healthy_weight < 30:
    print ('Overweight')
elif healthy_weight >= 30 and healthy_weight < 35:
    print ('Obese Level 1')
elif healthy_weight >= 35 and healthy_weight < 40:
    print ('Obese Level 2')
else:
    print ('Obese Level 3')
