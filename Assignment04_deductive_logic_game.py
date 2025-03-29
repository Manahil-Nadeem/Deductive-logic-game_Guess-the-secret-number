import streamlit as st
import random

# Function to provide feedback on the guess
def get_feedback(secret, guess):
    feedback = []
    
    # Check for correct digits in correct places (👌)
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("👌")
        elif guess[i] in secret:
            feedback.append("👍")
        else:
            feedback.append("❌")
    
    return ''.join(feedback)

# Main function to run the game
def play_game():
    # Custom styling for the background and title
    st.markdown("""
    <style>
        .stApp {
            background-color:#6495ED;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            font-style: italic;
            text-decoration: underline;
            Font family: Courier New (monospace)
            text-align: center;
        }
        .game-instructions {
            font-size: 20px;
            font-weight: normal;
            color: #333333;
            margin-bottom: 20px;
            font-style: italic;
            Font family: Georgia (serif)
        }
    </style>
    """, unsafe_allow_html=True)

    # Add custom title with bold, italic, and underline style
    st.markdown('<div class="title"> DEDUCTIVE LOGIC GAME:<br> GUESS THE SECRET <br>NUMBER GAME !</div>', unsafe_allow_html=True)
    
    # Initialize session state variables if they don't exist
    if "secret" not in st.session_state:
        st.session_state.secret = str(random.randint(100, 999))  # Generate a random 3-digit secret number
        st.session_state.attempts = 0  # Initialize attempts
        st.session_state.max_attempts = 10  # Maximum attempts
        st.session_state.game_over = False  # Game over flag
    
    # Display game instructions
    st.markdown('<div class="game-instructions">You have 10 attempts to guess the secret 3-digit number.</div>', unsafe_allow_html=True)
    
    # If game is over, display the result
    if st.session_state.game_over:
        st.write(f"Game Over! The secret number was {st.session_state.secret}.")
        if st.session_state.attempts < st.session_state.max_attempts:
            st.write("You guessed it correctly!")
        else:
            st.write("Sorry, you've used all attempts!")
        # Option to restart the game
        if st.button("Restart Game"):
            st.session_state.secret = str(random.randint(100, 999))
            st.session_state.attempts = 0
            st.session_state.game_over = False
    
    else:
        # Get user's guess (using Streamlit text_input instead of input())
        guess = st.text_input(f"Attempt {st.session_state.attempts + 1}/{st.session_state.max_attempts} - Guess a 3-digit number:")
        
        if guess:
            # Check if the input is a valid 3-digit number
            if len(guess) != 3 or not guess.isdigit():
                st.error("Please enter a valid 3-digit number.")
            else:
                # Update attempts
                st.session_state.attempts += 1
                
                # Check if the guess is correct
                if guess == st.session_state.secret:
                    st.success("👌👌👌 You Got IT! Correct number!")
                    st.session_state.game_over = True
                else:
                    # Provide feedback on the guess
                    feedback = get_feedback(st.session_state.secret, guess)
                    st.write(feedback)
                
                # If the player runs out of attempts
                if st.session_state.attempts == st.session_state.max_attempts:
                    st.session_state.game_over = True
                    st.write(f"Sorry! You've used all {st.session_state.max_attempts} attempts.")
                    st.write(f"The secret number was {st.session_state.secret}.")
            
# Start the game
if __name__ == "__main__":
    play_game()
