def process_friend_data():
    """Processes input for friends' data and queries their attributes efficiently."""
    test_cases = int(input().strip())

    for test_case in range(test_cases):
        num_friends, num_queries = map(int, input().split())
        friend_data = {}

        # Storing friend details in a dictionary
        for friend_index in range(num_friends):
            name, age, hobbies, chocolates = input().split()
            friend_data[name] = (age, hobbies, chocolates)

        # Querying stored friend details
        for query_index in range(num_queries):
            query_name = input().strip()
            if query_name in friend_data:
                age, hobbies, chocolates = friend_data[query_name]
                print(f"{age}, {hobbies}, {chocolates}")
            else:
                print("Friend not found")  # Optional error handling

if __name__ == "__main__":
    process_friend_data()
