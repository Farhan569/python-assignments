import streamlit as st
import re
import random
import string

#Custom Weights for Scoring
WEIGHTS = {
    "length": 2,
    "uppercase & lowercase": 2,
    "digits": 1,
    "symbols": 2
}

#Common Blacklisted Passwords
COMMON_PASSWORDS = set([
    '123456', 'password', '12345678', 'asdfghjkl', 'qwerty', 'abc123', '111111',
    '123123', 'admin', 'letmein', 'welcome', 'password1', 'iloveyou'
])

#Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("⚠️ Your password is too common. Avoid using popular passwords.")
        return 0, feedback

    # Length Check
    if len(password) >= 8:
        score += WEIGHTS["length"]
    else:
        feedback.append("❌ Password should be at least 8 character long.")

    # Uppercase & Lowercase
    if re.search(r"[A-Z]" and r"[a-z]", password):
        score += WEIGHTS["uppercase & lowercase"]
    else:
        feedback.append("❌ Include Uppercase & Lowercase letter.")

    # Digits
    if re.search(r"\d", password):
        score += WEIGHTS["digits"]
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += WEIGHTS["symbols"]
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&).")

    return score, feedback

#Password Generator
def generate_password(length=8):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

#Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter + Generator")

tab1, tab2 = st.tabs(["🔍 Check Password", "⚙️ Generate Password"])

#Password Checker Tab
with tab1:
    password = st.text_input("Enter your password", type="password")

    if password:
        score, feedback = check_password_strength(password)
        max_score = sum(WEIGHTS.values())

        # Score bar
        st.markdown(f"**Strength Score: {round(score, 1)} / {max_score}**")
        st.progress(score / max_score)

        if score < max_score * 0.6:
            st.warning("Your password needs improvement.")
            for tip in feedback:
                st.write(tip)
        elif score < max_score * 0.9:
            st.info("Decent password, but could be stronger.")
        else:
            st.success("✅ Great! Your password is strong.")

#Password Generator Tab
with tab2:
    st.write("Generate a strong, random password:")
    gen_length = st.slider("Password length", 8, 32, 12)
    if st.button("🔄 Generate Password"):
        new_pass = generate_password(gen_length)
        st.text_input("Your generated password:", value=new_pass, key="gen", type="default")
        st.code(new_pass)
        st.success("Copy and use this password wherever needed!")