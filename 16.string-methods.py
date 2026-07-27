# indexing = accessing elements of a sequence using [] (indexing operator)
            # [start:end:step]


# credit_card = "1234-5426-7756-9988"

# last_digit = credit_card[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digit}")

credit_card = "1234-5426-7756-9988"

last_digit = credit_card[::-1]
print(last_digit)