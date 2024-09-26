
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

def calculate_average_budget(movies):
    total_budget = sum(budget for _, budget in movies)
    average_budget = total_budget / len(movies)
    return average_budget

def identify_high_budget_movies(movies, average_budget):
    high_budget_movies = []
    for title, budget in movies:
        if budget > average_budget:
            difference = budget - average_budget
            high_budget_movies.append((title, budget, difference))
    return high_budget_movies

def main():
    print("Initial Movies Dataset:")
    for movie in movies:
        print(f"{movie[0]}: ${movie[1]:,}")

    
    average_budget = calculate_average_budget(movies)
    print(f"\nAverage Budget: ${average_budget:,.2f}")

   
    high_budget_movies = identify_high_budget_movies(movies, average_budget)
    print("\nHigh Budget Movies:")
    for title, budget, difference in high_budget_movies:
        print(f"{title}: ${budget:,} (Higher than average by ${difference:,})")

    print(f"\nTotal movies that exceeded the average budget: {len(high_budget_movies)}")

    
 
    num_movies_to_add = int(input("\nHow many movies would you like to add? "))
    for _ in range(num_movies_to_add):
            title = input("Enter the movie title: ")
            budget = float(input("Enter the movie budget: "))
            movies.append((title, budget))
        
        
    average_budget = calculate_average_budget(movies)
    print(f"\nUpdated Average Budget: ${average_budget:,.2f}")

    high_budget_movies = identify_high_budget_movies(movies, average_budget)
    print("\nUpdated High Budget Movies:")
    for title, budget, difference in high_budget_movies:
        print(f"{title}: ${budget:,} (Higher than average by ${difference:,})")

   
    print(f"\nTotal movies that exceeded the average budget: {len(high_budget_movies)}")
    
    

main()
