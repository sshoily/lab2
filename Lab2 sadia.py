def main():
    # Create a complex data structure
    about_me = {
        "full_name": "SADIA TABASSUM SHOILY", 
        "student_id": 10312016,
        "pizza_toppings": ["CHEESE", "MUSHRROM", "SAUSAGE"],
        "movies": [
            {"title": "dabbe", "genre": "horror"},
            {"title": "extraction", "genre": "action"}
        ]
    }
    
    # Add another movie to the data structure
    about_me["movies"].append({"title": "The Godfather", "genre": "horror"})
    
    # Add different toppings to the data structure
    different_toppings = ("onion", "green peppers", "olive")
    add_pizza_toppings(about_me, different_toppings)
    
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    print_movie_titles(about_me)
    print_movie_genres(about_me)

# Function that prints student name and ID    
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = "Sadia"
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me {first_name}.\nMy student ID is {student_id}.")

# Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    for topping in toppings:
        about_me["pizza_toppings"].append(topping.upper())  # Adding toppings in uppercase
    about_me["pizza_toppings"].sort()

# Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favorite pizza toppings are:")
    for topping in about_me["pizza_toppings"]:
        print("-", topping)  

# Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = ", ".join(movie["genre"].title() for movie in about_me["movies"])
    print(f"I like to watch {genres} movies.\n")

# Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    formatted_titles = ", ".join(movie["title"].title() for movie in about_me["movies"])
    print("Some of my favorite movies are:", formatted_titles, "!")


if __name__ == '__main__':
    main()
