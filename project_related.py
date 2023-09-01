# github_directory_viewer.py

import streamlit as st
import requests

def fetch_github_directory(repo_name):
    base_url = f"https://api.github.com/repos/{repo_name}/contents/"
    response = requests.get(base_url)
    return response.json()

def main():
    st.title("GitHub Directory Viewer")

    # Input fields
    repo_name = st.text_input("GitHub Repository Name", "Vipul4765/ipl-api-service")

    if st.button("Load Repository"):
        if repo_name:
            contents = fetch_github_directory(repo_name)
            if isinstance(contents, list):
                st.write(f"Contents of '{repo_name}' repository:")

                # Separate .py files and other files
                py_files = []
                other_files = []

                for item in contents:
                    if item['type'] == 'file':
                        if item['name'].endswith('.py'):
                            py_files.append(item)
                        else:
                            other_files.append(item)

                # Create two columns
                col1, col2 = st.columns(2)

                # Display directory files with buttons in the first column
                with col1:
                    st.write("Directory Files:")
                    for item in py_files:
                        if st.button(f"Show Code for {item['name']}"):
                            pass  # Add code to display .py file content here

                # Display a message or content for other files in the second column
                with col2:
                    st.write("Other Files:")
                    for item in other_files:
                        st.write(f"Other File: {item['name']}")
                        st.write("This is my project")

            else:
                st.error("Failed to fetch repository contents. Check your repository name.")
        else:
            st.warning("Please enter a valid GitHub repository name.")

if __name__ == "__main__":
    main()





'''import streamlit as st
import requests
import base64

repo_name = "Vipul4765/ipl-api-service"
file_name = "bowler_related.py"

url = f"https://api.github.com/repos/{repo_name}/contents/{file_name}"

response = requests.get(url)

if response.status_code == 200:
    content = response.json()['content']
    decoded_content = base64.b64decode(content).decode('utf-8')
    st.code(decoded_content)
else:
    print(f"Failed to fetch content for {file_name}")'''

