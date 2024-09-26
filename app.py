import pymongo
import streamlit as st

# MongoDB connection
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client["loginPage"]
collection = db["users"]

# Streamlit app title
st.title("🔐 MongoDB User Management")

# Sidebar with context and emojis
st.sidebar.title("📋 Operations Menu")
st.sidebar.write("""
Welcome to the **User Management App**! You can perform the following operations:
- ✍️ **Create**: Add new users to the database.
- 🔍 **Find**: Search for users by name.
- 🛠️ **Update**: Modify existing user details.
- 🗑️ **Delete**: Remove users from the database.
""")

# Sidebar selection for different operations
operation = st.sidebar.selectbox(
    "🔧 Choose an Operation",
    ["Create", "Find", "Update", "Delete"]
)


url = 'https://echoclone-ai.streamlit.app/'  # Replace with your desired URL
url1='https://anuragsportfolioassist.streamlit.app/'
st.markdown(
    """
    <style>
    .styled-text {
        font-size: 18px; /* Change font size */
        color: skyblue; /* Change text color */
        font-weight: bold; /* Make the text bold */
        
        margin-bottom: 20px; /* Add space below */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use markdown to display the styled text in the sidebar
st.sidebar.markdown('<p class="styled-text">Wanna explore my other AI Assistants? Check it out now!</p>', unsafe_allow_html=True)
# Adding a button to redirect to another URL
if st.sidebar.button('EchoClone AI🎧'):
    st.sidebar.markdown(f'You are being redirected to: [{url}]({url})', unsafe_allow_html=True)
    # Redirect using Streamlit's write function with HTML link and target="_blank"
    st.sidebar.write(f'<meta http-equiv="refresh" content="0;URL={url}" target="_blank">', unsafe_allow_html=True)

if st.sidebar.button('PortfolioAssist'):
    st.sidebar.markdown(f'You are being redirected to: [{url1}]({url1})', unsafe_allow_html=True)
    # Redirect using Streamlit's write function with HTML link and target="_blank"
    st.sidebar.write(f'<meta http-equiv="refresh" content="0;URL={url1}" target="_blank">', unsafe_allow_html=True)



# Create Operation
if operation == "Create":
    st.subheader("✍️ Create a New User")
    name = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")
    if st.button("Create User"):
        collection.insert_one({"name": name, "password": password})
        st.success(f"User {name} created successfully! 🎉")

# Find Operation
elif operation == "Find":
    st.subheader("🔍 Find a User")
    name = st.text_input("Enter username to search")
    if st.button("Search"):
        user = collection.find_one({"name": name})
        if user:
            st.write(f"✅ User **{name}** found with password: **{user['password']}**")
        else:
            st.error("❌ User not found!")

# Update Operation
elif operation == "Update":
    st.subheader("🛠️ Update User Information")
    name = st.text_input("Enter the current username")
    update_choice = st.radio("What would you like to update?", ["Username", "Password"])

    if update_choice == "Username":
        updated_name = st.text_input("Enter the new username")
        if st.button("Update Username"):
            collection.update_one({"name": name}, {"$set": {"name": updated_name}})
            st.success(f"Username updated from {name} to {updated_name} 🔄")
    elif update_choice == "Password":
        updated_password = st.text_input("Enter the new password", type="password")
        if st.button("Update Password"):
            collection.update_one({"name": name}, {"$set": {"password": updated_password}})
            st.success(f"Password updated for user {name} 🔑")

# Delete Operation
elif operation == "Delete":
    st.subheader("🗑️ Delete a User")
    name = st.text_input("Enter username to delete")
    if st.button("Delete"):
        collection.delete_one({"name": name})
        st.success(f"User {name} deleted successfully 🗑️")

# Display all users
if st.checkbox("👥 Show all users"):
    st.subheader("All Users:")
    users = collection.find()
    for user in users:
        st.write(f"👤 **Username**: {user['name']} | **Password**: {user['password']}")



st.markdown("""
    <hr style="border: none; border-top: 3px solid #bbb;">
    <div style="text-align:center;">
        <p>&copy; 2024 Anurag Srivatsav. All rights reserved.</p>
        <p>Connect with me on LinkedIn: <a href="https://linkedin.com/in/anuragsrivatsav" target="_blank">Anurag Srivatsav</a></p>
    </div>
""", unsafe_allow_html=True)
