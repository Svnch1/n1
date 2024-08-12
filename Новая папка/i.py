left_hand_keys = set('qazwsxedcrfvtgb')
right_hand_keys = set('yhnujmikolp')

def count_hand_usage(text):
    left_hand_count = 0
    right_hand_count = 0

    for char in text.lower():
        if char in left_hand_keys:
            left_hand_count += 1
        elif char in right_hand_keys:
            right_hand_count += 1

    return left_hand_count, right_hand_count

# Example usage:
with open('input.txt', 'r') as file:
    content = file.read()

left_count, right_count = count_hand_usage(content)
print(f"Left hand: {left_count}, Right hand: {right_count}")
