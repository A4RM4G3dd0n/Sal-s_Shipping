weight = 41.5

# Ground Shipping
if weight <= 2.00:
  print("Cost of ground shipping is: " + str(weight * 1.50 + 20))
elif weight > 2.00 and weight <= 6.00:
  print("Cost of ground shipping is: " + str(weight * 3.00 + 20.00))
elif weight > 6.00 and weight <= 10.00:
  print("Cost of ground shipping is: " + str(weight * 4.00 + 20.00))
elif weight > 10.00:
  print("Cost of ground shipping is: " + str(weight * 4.75 + 20.00))

# Premium Shipping
cost = 125.00
print("Cost of premium shipping: " + str(cost))

# Drone Shipping
if weight <= 2.00:
  print("Cost of drone shipping: " + str(weight * 4.50))
elif weight > 2.00 and weight <= 6.00:
  print("Cost of drone shipping: " + str(weight * 9.00))
elif weight > 6 and weight <= 10.00:
  print("Cost of drone shipping: " + str(weight * 12.00))
if weight > 10.00:
  print("Cost of drone shipping: " + str(weight * 14.25))
