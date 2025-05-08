# 🔐Assignment 02: Password Strength Meter

## **📌 Objective**  
Build a **Password Strength Meter** in Python that evaluates a user's password based on security rules. The program will:  
- Analyze passwords based on **length, character types, and patterns**.  
- Assign a **strength score** (Weak, Moderate, Strong).  
- Provide **feedback** to improve weak passwords.  
- Use **control flow, type casting, strings, and functions**.  

---

### **1. Password Strength Criteria**
A strong password should:  
✅ Be at least **8 characters long**  
✅ Contain **uppercase & lowercase letters**  
✅ Include at least **one digit** (0-9)  
✅ Have **one special character** (!@#$%^&*)  

### **2. Scoring System**
- **Weak (Score: 1-2)** → Short, missing key elements  
- **Moderate (Score: 3-4)** → Good but missing some security features  
- **Strong (Score: 5)** → Meets all criteria  

### **3. Feedback System**
- If the password is **weak**, suggest improvements.  
- If the password is **strong**, display a success message.  

---

### **🔹 Additionally

1. **Password Generator**: A feature to **suggest a strong password**.  
2. **User-Friendly Interface**: Use **Streamlit** for a GUI version.  
3. **Blacklist Common Passwords**: Reject weak passwords like "password123".  
4. **Custom Scoring Weights**: Give different **weights** to complexity factors.  
