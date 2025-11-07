from typing import Callable

import streamlit as st

st.title("Password checker")

conditions: dict[str, Callable[[str], bool]] = {
    "More than 8 characters": lambda pw: len(pw) > 8,
    "At least one uppercase letter": lambda pw: any(char.isupper() for char in pw),
    "At least one lowercase letter": lambda pw: any(char.islower() for char in pw),
    "At least one special character": lambda pw: any(char in "!@#$%^&*()_+-=;:/>.<," for char in pw),
    "At least one digit": lambda pw: any(char.isdigit() for char in pw),
}


def get_password_properties(password: str) -> dict[str, bool]:
    return {
        cond:eval(password) for cond, eval in conditions.items()
    }


user_input = st.text_input(label="Enter your password", type="password")

if st.button("Check password!"):
    if user_input:
        properties: dict[str, bool] = get_password_properties(user_input)

        for condition, passes in properties.items():
            if passes:
                st.success(f"Pass: {condition}")
            else:
                st.error(f"Fail: {condition}")
    else:
        st.write("Please enter a password.")
