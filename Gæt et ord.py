import streamlit as st
with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

ord = "hej"
guessed_letters = set()

st.write("The word contains", len(ord), "letters.")

while True:
    # Get user input
    user_input = st.text_input("Guess a letter")

    # Check if user input is a single letter
    if len(user_input) != 1:
        st.write("Please enter a single letter.")
        continue

    # Check if user has already guessed this letter
    if user_input in guessed_letters:
        st.write("You have already guessed this letter. Please try again.")
        continue

    # Add guessed letter to set of attempted letters
    guessed_letters.add(user_input)

    # Check if guessed letter is in the word
    if user_input in ord:
        st.write("Correct! The letter", user_input, "is in the word.")
    else:
        st.write("Sorry, the letter", user_input, "is not in the word.")

    # Check if all letters have been guessed
    if set(ord) == guessed_letters:
        st.write("Congratulations! You have guessed the word.")
        break

    # Display attempted letters
    st.write("Attempted letters:", sorted(guessed_letters))
