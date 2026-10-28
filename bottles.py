# 1 - We want a function that can start from any number (defaults to 99).
# 2 We start counting down from 99 all the way down to 1.
# 3 If current number is > 1: line 1 says "X bottles"
# If current number is 1: line 1 says "1 bottle" (singular)
# Then we check what number comes next (current number minus 1):
# If next number is > 1: line 2 says "Take one down... X-1 bottles..."
# If next number is 1: line 2 says "Take one down... 1 bottle..." (singular)
# If next number is 0: line 2 says "Take one down... no more bottles..."
# lastly 5 -  When the loop finishes (we're at 0), print the final store verse.

def bottle_song(num=99): # working with Linus I got to thinking what if I actually insert my variable into my defined function
    #  will use the range function to count backwards from num down to 1
    for i in range(num, 0, -1):
        # Determine whether the current count is singular or plural
        current_bottle = "bottle" if i == 1 else "bottles"
        
        # Print the first line of the verse - working with Linus and LaToya I realized I could use f-strings for clarity... and practice
        print(f"{i} {current_bottle} of beer on the wall, {i} {current_bottle} of beer.")
        
        # NEXT I will look at what the count will be after taking one down
        next_count = i - 1
        
        if next_count > 1: # This took me a while to get down right - re-reformated to use f-string
            print(f"Take one down and pass it around, {next_count} bottles of beer on the wall.")
        elif next_count == 1:
            print("Take one down and pass it around, 1 bottle of beer on the wall.")
        else:
            print("Take one down and pass it around, no more bottles of beer on the wall.")
            
    # Now we print the final verse once all bottles are gone
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print(f"Go to the store and buy some more, {num} bottles of beer on the wall.")

# run the functon
bottle_song()

# Linus mentioned using recursion would help solve this without a loop. I will look into that later because I was very please with my reformat above. re-committing not recursively 
####WOAH I'm Halfway there! Living on a prayer!