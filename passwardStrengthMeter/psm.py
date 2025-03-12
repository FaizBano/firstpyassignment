import streamlit as st
import re
import random
import string

# Blacklisted common passwords
BLACKLISTED_PASSWORDS = {"password", "123456", "qwerty", "password123", "letmein", "admin"}

# Generate a strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Check password strength
def check_password_strength(password):
    score = 0
    messages = []
    
    # Check for blacklisted passwords
    if password in BLACKLISTED_PASSWORDS:
        messages.append("❌ This password is too common. Choose a more secure one.")
        return 0, messages
    
    # Length Check (Weighted: 2 points)
    if len(password) >= 8:
        score += 2
    else:
        messages.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check (Weighted: 1 point)
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check (Weighted: 1 point)
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")
    
    # Special Character Check (Weighted: 2 points)
    if re.search(r"[!@#$%^&*]", password):
        score += 2
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, messages

# Streamlit UI
st.markdown("<h2 style='text-align: left; color: #FF5733; animation: typing 2s steps(50, end) forwards;'>🔒 Password Strength Checker & Generator</h2>", unsafe_allow_html=True)

st.markdown(
    "<style>"
    "@keyframes typing { from { width: 0; } to { width: 100%; } }"
    "h1 { overflow: hidden; white-space: nowrap; display: inline-block; }"
    "input[type='password'] { font-weight: bold; padding: 10px; font-size: 18px; border: 2px solid #FF5733; border-radius: 5px; }"
    "</style>",
    unsafe_allow_html=True
)

# Password Input
password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    result_style = "font-weight: bold; font-size: 20px; padding: 10px; border-radius: 5px;"
    if score >= 6:
        st.markdown(f"<p style='background-color: #d4edda; color: #155724; {result_style}'>✅ Strong Password!</p>", unsafe_allow_html=True)
    elif 4 <= score < 6:
        st.markdown(f"<p style='background-color: #fff3cd; color: #856404; {result_style}'>⚠️ Moderate Password - Consider adding more security features.</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='background-color: #f8d7da; color: #721c24; {result_style}'>❌ Weak Password - Improve it using the suggestions below.</p>", unsafe_allow_html=True)
    
    for msg in feedback:
        st.write(msg)

# Generate Strong Password Button
if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.text_input("Suggested Password:", value=strong_password, type="default")
