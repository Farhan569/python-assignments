import streamlit  as st
import hashlib
from cryptography.fernet import Fernet

if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()

cipher = Fernet(st.session_state.fernet_key)

if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}  # {"ciphertext": {"passkey": "hashed"}}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "authenticated" not in st.session_state:
    st.session_state.authenticated = True

# Hash the passkey using SHA-256
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)

    if encrypted_text in st.session_state.stored_data:
        if st.session_state.stored_data[encrypted_text]["passkey"] == hashed:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()

    st.session_state.failed_attempts += 1
    return None

st.sidebar.title("🔐 Navigation")
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Go to", menu)

if choice == "Home":
    st.title("🏠 Welcome to Secure Data Encryption System")
    st.write("Use this app to **securely store and retrieve text** with encrypted protection.")

elif choice == "Store Data":
    st.title("📂 Store Data")
    data = st.text_area("Enter your data:")
    passkey = st.text_input("Enter a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if data and passkey:
            encrypted = encrypt_data(data)
            hashed = hash_passkey(passkey)
            st.session_state.stored_data[encrypted] = {"passkey": hashed}
            st.success("✅ Data encrypted and saved successfully!")
            st.write("Here’s your encrypted data:")
            st.code(encrypted)
        else:
            st.error("⚠️ Please fill in both fields.")

elif choice == "Retrieve Data":
    if not st.session_state.authenticated:
        st.warning("🔒 Access denied. Please log in first.")
        st.stop()

    st.title("🔍 Retrieve Data")
    encrypted_input = st.text_area("Enter your encrypted data:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey:
            result = decrypt_data(encrypted_input, passkey)
            if result:
                st.success(f"✅ Decrypted Data: {result}")
            else:
                st.error(f"❌ Incorrect passkey! Attempts left: {3 - st.session_state.failed_attempts}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🚫 Too many failed attempts! Redirecting to login...")
                    st.session_state.authenticated = False
                    st.rerun()
        else:
            st.error("⚠️ Please fill in both fields.")

elif choice == "Login":
    st.title("🔑 Reauthorization Required")
    master_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if master_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.authenticated = True
            st.success("✅ Logged in successfully!")
            st.rerun()
        else:
            st.error("❌ Incorrect master password.")