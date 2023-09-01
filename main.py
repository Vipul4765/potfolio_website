import streamlit as st
import pandas as pd
from streamlit.runtime.state import widgets
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import project_related
import projects_decriptions
import boxes
import contact_info

st.set_page_config(layout='wide')



def load_lottie1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coder = load_lottie1('https://lottie.host/69aed16c-7cf5-46b9-beb6-50aee75e3535/1IH5t9bwIN.json')

st.write('##')
st.subheader('I am vipul Kumar')
st.title('My portfolio Website')
st.write('-----')

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'project', 'Certification', 'Contact'],
        icons=['person', 'code-slash', 'cc-square', 'chat-left-text-fill'],
        orientation='horizontal'

    )
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('🎓Undergraduate At SRM University')
            st.write("""Welcome! I'm a Python enthusiast skilled in utilizing essential libraries like NumPy, Pandas, 
            Matplotlib, Seaborn, and MySQL. Through various projects, I've harnessed these tools to analyze data and 
            create insightful visualizations. My passion lies in unraveling the narratives within datasets, 
            approaching challenges with a detail-oriented and solution-driven mindset. I navigate the 
            dynamic world of data, consistently seeking innovative ways to contribute and grow.""")
            st.write("----------")
            skills = ['Python', 'MySql', 'Numpy', 'Pandas', 'Matplotlib', 'Seaborn', 'C++', 'DSA', 'OOPs', 'Streamlit',
                      'Flask', 'Html']

            # Display the Skills section
            st.title('🔥Skills')

            # Display skills buttons in rows
            boxes.create_skill_buttons(skills)

        with col2:
            with col2:
                col1, col2 = st.columns(2)
                with col2:
                    st_lottie(lottie_coder, width=350, )  # Adjust width and alignment
                st.write('---')
                st.header("👨‍💻Coding Profile")
                st.markdown("- [GFG](https://auth.geeksforgeeks.org/user/vipuldhankar)")
                st.markdown("- [Leetcode](https://leetcode.com/coder_123_/)")
                st.markdown("- [CodeChef](https://www.codechef.com/users/vipuldhankar17)")
                st.markdown("- [Hackerrank](https://www.hackerrank.com/vipuldhankar1711)")
                st.markdown(
                    "- [Coding Ninja](https://www.codingninjas.com/studio/profile/a732a5a7-88e5-44ab-9eaf-4af8a4cb59ff)")

        st.write('-----')
        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.header("Education")
                education_df = pd.DataFrame({
                    'Education': ['B.Tech', 'XII', 'X'],
                    'Passing Year': [2024, 2019, 2017],
                    'Grade': ['8.86 CGPA', '66.6%', '7.8 CGPA'],
                    'Board': ['SRMIST', 'CBSE', 'CBSEs']
                })
                st.table(education_df.style.set_properties(**{'text-align': 'center', 'width': 'auto'}))

            with col4:
                st.write('#')
                st.write('#')
                st.code("""
                passion = "I find my passion in coding and problem-solving!"
                print(passion)
""")
    st.write('##')
    with st.container():
        col5, col6 = st.columns(2)

        pass

if selected == 'Certification':
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            selected = option_menu(
                menu_title="Please choose from the options below and click to view the awarded certificate",
                options=['Python', 'DSA', 'Data Analysis', 'Pandas', 'OOPs'],
                icons=['code-square', 'code-square', 'code-square', 'code-square', 'code-square'],
            )

        if selected == 'Python':
            with col2:
                st.image('CN_Certificate_914cbfc05b28dfd9 (1)_page-0001.jpg', caption='Coding Ninjas Certificate',
                         use_column_width=True)

        if selected == 'DSA':
            with col2:
                st.image('NPTEL DSA_page-0001.jpg')
        if selected == 'Data Analysis':
            with col2:
                st.image('Data Analysis_page-0001.jpg')
        if selected == 'Pandas':
            with col2:
                st.image('Pandas_page-0001.jpg')
        if selected == 'OOPs':
            with col2:
                st.write('no available yet')

st.write('----')
if selected == 'project':
    project_name = 'Project : IPL API'
    st.title(project_name)


    col1, col2 = st.columns(2)
    with col1:

        # calling project description function
        subheading_style = "color: #000000; text-decoration: underline;"
        st.markdown(f"<h4 style='{subheading_style}'>Project Description:</h4>", unsafe_allow_html=True)
        projects_decriptions.ipl_api()




    with col2:
        stack = ['Flask', 'Python', 'Pandas', 'Numpy', 'Data Analysis', 'Kaggle']

        boxes.create_skill_buttons(stack)
        project_related.main()
if selected == 'Contact':
    contact_info.create_streamlit_content()
