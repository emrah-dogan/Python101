#This is a small program that calculates the percentage of the likes of a social media post.

#Calculates rating percentage.
def rating_calc():
    global rating
    rating = (like_num / (like_num + dislike_num)) * 100

#Prints a comment about the overall reaction to the post.
def rating_printer():
    if rating >= 90:
        print("Very positive!")
    elif rating > 50:
        print("Positive!")
    elif rating == 50:
        print("Neutral.")
    else:
        print("Negative!")

#Takes input from the user.    
def user_input():
    global like_num
    global dislike_num

    print("Please enter the number of likes: ")
    try:
        like_num = int(input())
    except ValueError:
        print("You have to enter a numerical value: ")
        user_input()
    
    print("Please enter the number of dislikes: ")
    try:
        dislike_num = int(input())
    except ValueError:
        print("You have to enter a numerical value: ")
        user_input()

print("Hello!")
user_input()
rating_calc()
print("Rating value: ", rating)
rating_printer()