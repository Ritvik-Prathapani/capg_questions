def count_coins():
    """Counts occurrences of unique coin values and prints them in sorted order."""
    num_coins = int(input().strip())
    coin_counts = {}

    for coin_index in range(num_coins):
        coin_value = int(input().strip())
        coin_counts[coin_value] = coin_counts.get(coin_value, 0) + 1  # Optimized dictionary update

    # Print sorted coin counts
    for coin_value, count in sorted(coin_counts.items()):
        print(coin_value, count)

if __name__ == "__main__":
    count_coins()
