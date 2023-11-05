import streamlit
# Now you can import option_menu # This is ready
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
from streamlit.runtime.state import widgets
import requests
from streamlit_lottie import st_lottie
import project_related
import projects_decriptions
import boxes
import contact_info

st.set_page_config(layout='wide', page_title="My Portfolio Website", page_icon="🚀")




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


            # List of technologies
            #tech1
            st.header('💼SKILLS')
            st.code(
                """
                'Python🐍   SQL🐬   C++🖥️   HTML🌐'
                'Numpy🧮   Pandas🐼   Matplotlib📈   Seaborn📊'
                'DSA📚   OOPs🧪   Git🐙   Github🐙'
                'Streamlit🔮   Flask🌐   Tableau📊'
                'Machine Learning 🤖   Backened Developer💼   RestApi🌐'
                
                """

            )
            # Display skills buttons in rows
            #boxes.create_skill_buttons(skills)

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
                menu_title="click to view the awarded certificate",
                options=['Python', 'DSA', 'Mysql Beginner', 'MySql Intermediate', 'Problem Solving Basic Certificate' ,'Problem Solving Intermediate Certificate' ,'Data Analysis', 'Pandas'],
                icons=['code-square', 'code-square', 'code-square', 'code-square', 'code-square', 'code-square', 'code-square', 'code-square', 'code-square'],
            )

        if selected == 'Python':
            with col2:
                st.image('CN_Certificate_914cbfc05b28dfd9 (1)_page-0001.jpg', caption='Coding Ninjas Certificate',
                         use_column_width=True)
                st.markdown('------------------------------------------------------------------------------------------Verify at : [link](https://ninjasfiles.s3.amazonaws.com/certificate275017976f6c891eb495cdbfa5db8745b992116.pdf)')

        if selected == 'DSA':
            with col2:
                st.image('NPTEL DSA_page-0001.jpg', caption = 'NPTEL Certificate')
                st.markdown('------------------------------------------------------------------------------------------Verify at : [link](https://drive.google.com/file/d/1m7J5pY9VGkKaS6RUgXlBg-MbEjPPlrCN/view)')
        if selected == 'Data Analysis':
            with col2:
                st.image('Data Analysis_page-0001.jpg')
        if selected == 'Pandas':
            with col2:
                st.image('Pandas_page-0001.jpg')


        st.write(
            f'<style>div.stButton > button:first-child {{ position: fixed; top: 0; right: 0; }}</style>',
            unsafe_allow_html=True
        )

        if selected == 'Mysql Beginner':
            with col2:
                st.image('sql_basic certificate_page-0001.jpg', caption="Vipul Kumar's HackerRank Certificates")
                st.markdown('------------------------------------------------------------------------------------------Verify at : [link](https://www.hackerrank.com/certificates/4fefbc6b8162)')

        if selected == 'MySql Intermediate':
            with col2:
                st.image('sql_intermediate certificate_page-0001.jpg', caption= "Vipul Kumar's HackerRank Certificates")
                st.markdown('------------------------------------------------------------------------------------------Verify at : [link](https://www.hackerrank.com/certificates/7781b740714d)')

        if selected == 'Problem Solving Basic Certificate':
            with col2:
                st.image('problem_solving_basic certificate_page-0001.jpg', caption= "Vipul Kumar's HackerRank Certificates")
                st.markdown('------------------------------------------------------------------------------------------Verify at : [link](https://www.hackerrank.com/certificates/0d2f352f87e0)')

        if selected == 'Problem Solving Intermediate Certificate':
            with col2:
                st.image('problem_solving_intermediate certificate_page-0001.jpg', caption="Vipul Kumar's HackerRank Certificates")
                st.markdown('------------------------------------------------------------------------------------------Verify at : [link](https://www.hackerrank.com/certificates/bb46e0b2d12d)')

st.write('----')
if selected == 'project':
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            selected = option_menu(
                menu_title=None,
                options=['12TH MAN', 'Inshort News Clone', 'Using Tableau', 'My NLP APP', 'My Porfolio Website', 'Face Detection', 'Flight Dashboard'],
                icons=['code-slash', 'code-slash', 'code-slash', 'code-slash', 'code-slash', 'code-slash','code-slash'],


            )

    if selected == 'My Porfolio Website':
        with col2:
            st.subheader('My Porfolio Website')
            stack = ['Python', 'Streamlit', 'Hosting']
            boxes.create_skill_buttons(stack)
            st.write('#')
            st.write('📈Key Features:-')
            st.write("- 🚀 As a developer, I've harnessed the power of Streamlit to create my own dynamic portfolio website. 🌐")
            st.write("- 💼 On my site, you'll find a collection of my projects and experience neatly organized for easy navigation. Explore my Projects section to see my work in action.")

        col34, col35 = st.columns(2)
        with col34:
            col1, col2= st.columns(2)
            with col1:
                st.image('Portfolio1.png')
            with col2:
                st.image('portfolio2.png')
            col3, col4 = st.columns(2)
            with col3:
                st.image("portfolio3.png")
            with col4:
                st.image('portfolio4.png')


        with col35:
            st.write("- 🎓 I'm committed to lifelong learning and have earned several certificates in the tech industry. Head over to my Certificates section to see my qualifications.")
            st.write("- 📈 With interactive charts and visuals, I've made it simpler for visitors to understand my work and skills.")

            st.write("- 👉 [Check it out here](https://mainpy-kvjdrm8gh65vqodkzoueyb.streamlit.app/).")

            st.write("- 🤝 I'm always looking to connect with fellow professionals, so please feel free to send me a connection request.")
            st.write("- 📌 Let's explore opportunities and collaborations together!")

    if selected == 'Face Detection':
        with col2:
            st.write('update soon')

    if selected == 'My NLP APP':
        with col2:
            st.subheader('My NLP APP')
            stack = ['Python', 'Api Integration', 'GUI', 'NLP']
            boxes.create_skill_buttons(stack)
            st.write(
                "I leverage advanced Natural Language Processing (NLP) techniques and APIs for sentiment analysis, NER, and emotion detection in text. My projects involve harnessing the power of AI to understand and interpret human language, providing valuable insights into people's feelings and sentiments")
            st.write('📈Key Features:-')
            st.write('- 📚 Proficient in Natural Language Processing (NLP) techniques.')
            st.write('- 🧬 Utilize APIs for sentiment analysis, Named Entity Recognition (NER), and emotion detection in text.')
            st.write("- 📊 Provide valuable insights into people's feelings and sentiments through text analysis.")
            st.markdown('- [Githhub Respository](https://github.com/Vipul4765/nlppython)')
    if selected == 'Flight Dashboard':
        with col2:
            st.write('Update Soon')


    if selected == 'Inshort News Clone':
        with col2:
            st.title('Inshort News Clone')
            stack = ['Python', 'Tkinter', 'API Integration', 'Request Library', 'webbrowser', 'PIL']
            boxes.create_skill_buttons(stack)
            st.write("I'm a Python developer who created 'Mera News App,' a user-friendly news application. It provides real-time news updates with images, headlines, and descriptions. Stay informed and explore the world's latest news with ease")
            st.markdown('- [Githhub Respository](https://github.com/Vipul4765/inshort-news-application.git)')
        col34, col35 = st.columns(2)
        with col34:
            col1, col2 = st.columns(2)
            with col1:
                st.image('Insort1.png')
            with col2:
                st.image('Insort2.png')
        with col35:
            st.write('📈Key Features:-')
            st.write("- Live News: Get real-time news updates from various sources.")
            st.write("- Live News: Get real-time news updates from various sources.")
            st.write("- Live News: Get real-time news updates from various sources.")
            st.write("- User-Friendly: The app provides a clean and intuitive user interface.")

    if selected == '12TH MAN':
        with col2:
            project_name = '12TH MAN'
            st.subheader(project_name)
            stack = ['Flask', 'Python', 'Pandas', 'Numpy', 'Data Analysis', 'MySQL', 'API Development', 'Backened Dev', 'API Testing']
            boxes.create_skill_buttons(stack)
            st.write('Introducing 12TH MAN IPL API Service—a treasure trove of cricket data! You can use my API to build your fantastic app, enhance your cricket website, or simply explore cricket data.')
            st.markdown("- [Github Respository](https://github.com/Vipul4765/ipl-api-service)")
        col34, col35 = st.columns(2)
        with col35:

            # calling project description function
            subheading_style = "color: #000000; text-decoration: underline;"
            projects_decriptions.display_project_description()








            project_related.main()

    if selected == 'Using Tableau':
        with col2:
            st.header('IPL DASHBOARD')
            stack = ['Tableau', 'Data Analysis', 'MySQL']
            boxes.create_skill_buttons(stack)
            st.subheader('About Project')
            st.write('📊 Explore the IPL like never before! My Tableau IPL data project is now live, offering dynamic data trends at your fingertips. Dive into cricket insights with the power to choose.')
            st.markdown(
                '- [Click here for Tableau DashBoard](https://public.tableau.com/app/profile/vipul.kumar2288/viz/12thMan/Story1)')
        col3, col4 = st.columns(2)
        with col3:
            col1,col2 = st.columns(2)
            with col1:
                st.image('Overall_tableau.png')
            with col2:
                st.image('Batsman_tableau.png')
            col3, col45, col5 = st.columns(3)
            with col3:
                st.image('Bowler_tableau.png')
            with col45:
                st.image('Bats_vs_Bow_tableau.png')
            with col5:
                st.image('Bats_vs_Bowler_tableau.png')
        with col4:
                st.write('In story there are five dashboard :-')
                st.write('''1.Overall  
                            2.Batsmen  
                            3.Bowlers  
                            4.Batsmen vs. Bowlers  
                            5.Batsmen vs. Stadium''')
                st.write('📈Key Features:-')
                st.write('- Customize your analysis by selecting players, teams, or seasons  ')
                st.write('- Interactive dashboards for hands-on data exploration')
                st.write('- In-depth coverage of multiple IPL seasons')
                st.markdown('- [Video Link To see Project](https://www.loom.com/share/da892138440f4cb7aa108ba68915710e?sid=dd779a16-8a6e-46d9-9cd6-dad64564ec3c)')




if selected == 'Contact':
    contact_info.create_streamlit_content()



