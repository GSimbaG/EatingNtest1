import streamlit as st

# Your Snowflake Logic: Eater and eaten numbers
board = {
    "Top Left": {"eater": 2, "eats": [1, 10]},
    "Top Right": {"eater": 5, "eats": [1, 7]},
    "Bottom Left": {"eater": 2, "eats": [4, 8]},
    "Bottom Right": {"eater": 6, "eats": [1, 9]},
    "Center": {"eater": 3, "eats": []}
}

st.title("❄️ My Snowflake: Eating Number Grid")

st.write("Click any corner to reveal what numbers it has eaten.")

# Store which parts have been revealed
if "revealed" not in st.session_state:
    st.session_state["revealed"] = {
        "Top Left": False,
        "Top Right": False,
        "Bottom Left": False,
        "Bottom Right": False
    }

# Define toggle function
def toggle_reveal(corner):
    st.session_state["revealed"][corner] = not st.session_state["revealed"][corner]

# Layout: Grid of 3x3 using columns
col1, col2, col3 = st.columns(3)

with col1:
    if st.button(f"Top Left: {board['Top Left']['eater']}"):
        toggle_reveal("Top Left")
    if st.session_state["revealed"]["Top Left"]:
        st.write("Eats:", board["Top Left"]["eats"])

with col2:
    st.write(f"Center: {board['Center']['eater']}")

with col3:
    if st.button(f"Top Right: {board['Top Right']['eater']}"):
        toggle_reveal("Top Right")
    if st.session_state["revealed"]["Top Right"]:
        st.write("Eats:", board["Top Right"]["eats"])

with col1:
    if st.button(f"Bottom Left: {board['Bottom Left']['eater']}"):
        toggle_reveal("Bottom Left")
    if st.session_state["revealed"]["Bottom Left"]:
        st.write("Eats:", board["Bottom Left"]["eats"])

with col3:
    if st.button(f"Bottom Right: {board['Bottom Right']['eater']}"):
        toggle_reveal("Bottom Right")
    if st.session_state["revealed"]["Bottom Right"]:
        st.write("Eats:", board["Bottom Right"]["eats"])

# Reset button
if st.button("Reset"):
    for corner in st.session_state["revealed"]:
        st.session_state["revealed"][corner] = False
