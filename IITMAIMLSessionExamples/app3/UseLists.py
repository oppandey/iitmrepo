print("Welcome to Python")

#Write an application to create and perform list operations
customer_feedback_options = ["Excellent","Good","Bad","Not Satisfied"]
print(customer_feedback_options[0])#get specific value
print(customer_feedback_options)
print(customer_feedback_options[-1])

#Iterate through list
for feedback in customer_feedback_options:
    print(feedback)
#extract specific range of values
sliced_list = customer_feedback_options[1:3]
print(sliced_list)
print(len(customer_feedback_options))
customer_feedback_options.append("Superb")
print(customer_feedback_options)