import streamlit as st
from pathlib import Path

st.set_page_config(initial_sidebar_state="expanded")

pages = ["About Me",
        "Education",
        "Work Experience",
        "Skills and Competencies",
        "Projects",
        "Programming & Development",
        "Certifications, Achievements, & Spotlights",
        "Publications & Webinars",
        "Professional Goals",
        "Contact"]

st.sidebar.title("Navigation")
page_selection = st.sidebar.selectbox("Select a page", pages)

st.sidebar.write("Quick Links")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

st.sidebar.download_button(
    "Download Latest Resume",
    data=(DATA_DIR / "paladino_resume_20260101.pdf").read_bytes(),
    file_name="Andrew_Paladino_Resume.pdf",
    mime="application/pdf",
)

st.sidebar.link_button(
    "LinkedIn",
    url="https://www.linkedin.com/in/andrewpaladino1/",
    use_container_width=False,
)

st.sidebar.link_button(
    "GitHub",
    url="https://github.com/ajpaladi",
    use_container_width=False,
)

st.sidebar.link_button(
    "Drone Photography Instagram",
    url="https://www.instagram.com/tipsypilot/",
    use_container_width=False,
)

st.sidebar.link_button(
    "Etsy Shop",
    url="https://www.etsy.com/shop/tipsypilot",
    use_container_width=False,
)

st.sidebar.link_button(
    "Analytics Blog",
    url="https://medium.com/@andyjpaladino",
    use_container_width=False,
)

if page_selection == "About Me":

    st.title("Welcome to my Portfolio!")
    st.image(DATA_DIR / "IMG_0358.jpg", caption="Portrait of Andy, Fall, 2025")

    st.subheader("About Me")
    st.write("""
            Hey there…
            
            I am currenly a Senior Data Engineer @ Atreides, a Canadian-based IOT startup company in the defense sector.
            In my relatively young professional career, I've worked in nearly every professional setting, from small 
            startups to large corporations, from government contracts to private industries. 
            I spent about 4 years in the startup drone indutry and my last 5 in the adtech space. My undergraduate educational 
            background was primarly in Geographic Information Systems, since graduatining in 2018 and being a member of 
            highly technical teams, I've evolved into a senior engineer, polishing my edges along the way with my recent 
            completion of an M.S. in Data Analytics and Computer Science from George Washington University's School of 
            Engineering and Applied Science. I am highly motivated, technical individual who exels in fast-paced, dynamic environments surrounded by engineers. 
            I thrive at leading teams in R&D, rapid prototying, and solutions engineering, excelling at driving new product into platform capabilities.
            I am best suited as a front-line technical leader for customers, solving problems and providing solutions management. 
            
            Fun Facts:
            - I'm from Morgantown, West Virginia. Country roads, take me home!
            - I started my career as Master Planning Intern for Walt Disney Imagineering.
            - I am a drone photographer and surveyor, and have been flying drones for over 10 years. I have a large collection of drone photos, and have been featured in several publications.
            - I ran division I cross country and track at Syracuse University. In 2015, my team won the NCAA D1 National Title. 
            - I was a childhood stage actor, mostly regional musical theater performances. 
        """)
    
elif page_selection == "Education":
    
    st.title("Education")
    st.subheader("Graduate Studies and Continued Education")
    st.write("M.S. in Data Analytics and Computer Science, School of Engineering and Applied Science, George Washington University, 2026")
    st.write("GPA: 3.88, Summa Cum Laude")
    st.write("""
             
             Coursework:
                - Uncertainty Analysis For Engineers
                - Programming for Analytics
                - Big Data for Engineers
                - Data Mining
                - Database Management Systems
                - Cloud Computing
                - Spatial Statistics
                - Algorithms & Graph Theory
                - Applied Machine Learning
                - Capstone Research: Agentic Geospatial Large Language Model
             
             """)

    st.subheader("Undergraduate Studies")
    st.write("B.S. in Geographic Information Systems, Maxwell School of Citizenship and Public Affairs, Syracuse University, 2018")
    st.write("Minor in Public Communications, Newhouse School of Public Communications, Syracuse University, 2018")
    st.write("GPA: 3.3")
    st.write("""
             Coursework:
             Major: Geographic Information Systems`
             - 3D Geographic Information Systems
             - Cartographic Design
             - Global Environmental Change
             - Political Geography
             - Human Geography
             - Spatial Storytelling
             - Sustainable Science and Policy 
             - The Anthropocene: Humans and the Environment
             - The Natural Environment
             - Introduction to Geographic Information Systems
             Minor: Public Communications
             - Real News, Fake News
             - Visual Issues in the Media 
             - Communications Law
             - Advertising 
             - Global Persuasion
             - Public Advocacy
             """)
    
elif page_selection == "Work Experience":
    
    st.title("Full-Time Work Experience")

    st.subheader("Senior Data Engineer, Atreides")
    st.write("Dates: 2025 - Present")
    st.write("Industry & Sector: Defense, Startup")
    st.write("Technologies: Python, PySpark, SQL, Temporal, Kubernetes, Docker, AWS EC2/RDS, PostgreSQL")
    st.write("""
             
             Responsibilities/Accomplishments:

             - Hired to lead R&D and prototyping efforts for the Atreides Data Engineering Team with a focus on the technical platform implementation of new customer solutions and products. 
             - Expanded Atreides product porfolio offerings that deviated from core data pipeline deliverables using our Adhoc Orchestration Pipeline. 
             - Ideated, developed, and expanded on Atreides internal tooling suite, enabling internal stakeholders such as analysts, engineers, and product to 10x their efficiency and output.
             - Developed and shipped Atreides' first suite of products derived solely from AIS data.
             - Led the technical development and deployment of osint-derived geospatial data products that were integrated the core analyst suite. 
             - Spearheaded the first iteration of core Atreides data science algorithms and capabilities.


             """)
    st.subheader("Solutions Engineer III, Sierra Nevada Corporation")
    st.write("Dates: 2024 - 2025")
    st.write("Industry & Sector: Defense & Space, Private")
    st.write("Technologies: Python, PySpark, SQL, Databricks, AWS EC2/RDS")
    st.write("""
             
             Responsibilities/Accomplishments:

             - Proactively provided technical and analytical support, solutioning, onboarding, and success for dozens of commercial and federal clientele + prospects. 
             - Pioneered the development and maintenance of several internal python API wrappers that contain normalization, analytical, and visualization functions and methods for customer facing products, one of which is now being utilized by multiple internal technical stakeholders for simple, intuitive, and quick API interaction. The wrapper allowed me to invent and test innovative solutions that often paved the way for new on-platform product road mapping and development
             - Led the technical solutioning and implementation of internal and external facing marketing products and strategies, leveraging data to produce advanced audience metrics and demographic insights
             - Led the technical development, visualization, and deployment of an ETL-based dashboarding solution for federal stakeholders, incorporating insights from self trained and deployed LLMs using Ollama & HuggingFace
             - Facilitated technical QA efforts prior to and following product release, bugs, updates.
             
             """)
    
    st.subheader("Product Manager, Zietview")
    st.write("Dates: 2023 - 2024")
    st.write("Industry & Sector: Commerical Drone, Startup")
    st.write("Technologies: Python, SQL, Figma, AHA")
    st.write("""
            
            Responsibilities/Accomplishments:
             
            - Led Zeitview's Platform Team of developers, designers, and QA members in the scoping, development, and deployment and of products, features, and enhancements associated with Zeitview's enterprise platform, Admin. 
            - Maintained cross-functional collaboration with operations and finance to understand the needs that influenced prioritization on the product roadmap. 
            - Worked with vertical product managers to ensure that platform was successfully supporting each branch application (solar, wind, properties, etc.) 
            - Developed a python application to deliver sprint metrics on for each product-managed vertical every 2 weeks.

            """)
    
    st.subheader("Solutions Engineer, Orbital Insight")
    st.write("Dates: 2022 - 2023")
    st.write("Industry & Sector: Commerical IOT, Startup")
    st.write("Technologies: Python, SQL, AWS EMR, AWS EC2/RDS")
    st.write("""
        
        Responsibilities/Accomplishments:
            
        - Promoted to Solutions Engineer, an expansion of my role as a Technical Customer Success Manager. 
        - Managed the technical workflows for ALL of Orbital's commercial clientele, often building, testing, updating, and delivering new and existing technical, custom solutions & products associated with Orbital's professional services portfolio.
        - As a Technical Customer Success Manager on the Solutions Engineering Team @ Orbital Insight, I played a critical, hybrid role between a CSM and an SE. 
        - I supported over 2 dozen clients in a broad range of responsibilities, ranging anywhere from general account management to professional services and geospatial data analysis (via python & notebooks) on an enormous variety geolocation datasets (Cell, Connected Car, ADSB, AIS) and satellite imagery. 
        - The hybrid aspect of the role allowed me to improve on and flourish in my python & data science proficiency, as I had the flexibility to script as often as possible (daily at times), providing multitudes of business solutions to customers and their use-cases in the process. My findings, exploration, and analysis of AIS (data from ships) led to a 4 part blog series and a follow webinar that can be found on Orbital Insight's website.

        """)

    st.subheader("GIS Support Engineer, Mapware")
    st.write("Dates: 2021 - 2022")
    st.write("Industry & Sector: Commercial Drone, Startup")
    st.write("Technologies: Python, SQL, ArcGIS Pro, ArcPy, Salesforce Lightning Service, Agisoft Metashape")
    st.write("""
    
    Responsibilities/Accomplishments:
             
    - Helped Mapware establish and deploy a functional Customer Success Department, implementing CRM/Case Management best practices (via Salesforce Lightning Service). 
    - Spearheaded Case Management efforts across the org (Technical Support -> Product -> Engineering), ensuring the clients' questions, feedback, and any bugs were prioritized and solved in a functional manner. 
    - I created and deployed a public-facing knowledge base and digital experience for both commercial and federal customers, and utilized GIS and photogrammetric tools/best practices to troubleshoot customer datasets. 
    - I helped to create and managed all GIS workflows pertaining to the Air Force STRATFI Project, specifically as an input to ML and AI model building for habitat and species detection. 
    - Spearheaded data collection efforts in the field with RGB/LiDAR/MS equipped multirotor and fixed-wing (NDAA Compliant) UAS
             
    """)

    st.subheader("Geospatial/Drone Data Analyst, Woolpert")
    st.write("Dates: 2020 - 2021")
    st.write("Industry & Sector: Defense Contracting, Private")
    st.write("Technologies: Python, SQL, ArcGIS Pro, ArcPy, Pix4D")
    st.write("""

    Responsibilities/Accomplishments:
             
    Andrews Air Force Base | 316th CES/CEN Geospatial Specialist II & Geospatial Integration Office (GIO) Support:
    - Led the geospatial implementation, automation, product creation and delivery efforts for the 316th CES and GeoBase Execution Support Office @ Joint Base Andrews. 
    - As the sole data steward for the JBA Enterprise Geodatabase, I was tasked to manage airmen, assign roles, maintain records, modernized workflows, and develop new products/capabilities that were utilized by JBA in effort to track all assets maintained by the Squadron.

    Air Force Civil Engineering Center (AFCEC) | SUAS Office - Data Processing & Analysis Subject Matter Expert:

    - Aside from my roles @ JBA, I was appointed by AFCEC to help acquire funding for, develop, and establish both an sUAS Office and a Drone-As-A-Service (DaaS) Provider, at large, to support advanced sUAS surveying capabilities at Air Force Installations around the United States and Overseas. 
    - My role within the office is specifically to develop post-flight data processing/analysis workflows and subsequent data products for vendors across the AF.           
                
    """)

    st.subheader("Drone Data Analyst/Product Manager, Measure UAS")
    st.write("Dates: 2019 - 2020")
    st.write("Industry & Sector: Commercial Drone, Startup")
    st.write("Technologies: Python, SQL, ArcMap, ArcPy, AutoCAD Civil 3D, Mapbox SDK's, Pix4D")
    st.write("""

    Responsibilities/Accomplishments:
             
    Data Product Manager:
    - In addition to my existing duties as a GIS/Drone Data Analyst at Measure UAS, my position evolved into that of a Data Product Manager and AutoCAD SME when the Data Engineering team at Measure Inc. was acquired by Aerodyne Group in late 2019. 
    - As a Data Product Manger and AutoCAD SME, my duties included: Oversaw the production, development, deployment and data processing tasks for our drone-based AutoCAD Rooftop Inspection Product. 
    - I currently manage a team of 5+ CAD professionals (Aerodyne Group) based in Malaysia to aid this workflow. Co-Managed a Solar O&M Inspection Product that is currently in the development phases. 
    - The product will be used to service the solar industry in the data capture, inspection, auto-detection and deployment of a reports that are based on hotspots/anamolies found on thermal images. 
    - Managed clients on a daily basis, as the role in general is largely client facing. I am in direct contact with the client from the time a sale has been made to the time a project is complete or product is delivered. 
    - This task requires incredible communication skills, good maintenance and of customer/client relationships, and critical deadline management.

    GIS & Drone Data Analyst:
    - Assisted the Data Engineering Team with the processing, modeling, inspection, and delivery of a multitude of the company's solar products using high level GIS tools (ArcMap, ArcGIS Online, Web Map Developer), Drone Software platforms (Emotion, Pix4D), and scripting software to aid the workflow (Python 3, PyCharm, Notepad ++)
    - Modeled, inspected, and annotated damage on large-scale solar sites, ranging from 1mW to 50 mW's using thermal data collected in the field via drone.
    - Used prior piloting experience and airspace knowledge, I aided Flight Operations in the field by conducting drone flights (Phantom 4 Pro, Inspire I) to acquire RGB and thermal data for R&D/client-specific requests.
    - Led the design and integration of a digital data product for a client using Mapbox SDK’s. The product visualized the construction progress of a site over time and incorporated clickable timestamps, orthomosaics, and interactive aerial panoramas. 
    - Used AutoCad Civil 3D to draft, design, edit, and update .dwg files for the design and implementation of client-based solar rooftop installments. Improved the company's pitched-rooftop AutoCAD product for solar installments. 
    - Assisted the T&D Inspection workflow and the T&D integration into Scopito. Used drone data to inspect and annotate damage on miles of T&D lines.
                
    """)

    st.title("Internships")
    
    st.subheader("Master Planning GIS Internship, Walt Disney Imagineering")
    st.write("Dates: 2018 - 2019")
    st.write("Industry & Sector: Commercial Entertainment, Public")
    st.write("Technologies: ArcGIS Pro, ArcMap, AutoCAD, Adobe Illustrator, Photoshop, LIDAR")
    st.write("""
             
    Responsibilities/Accomplishments:
             
    - Used GIS and planning tools (ArcGIS Pro, ArcMap, AutoCAD) to conduct analysis on property-wide datasets. 
    - Used GIS to develop reports (Adobe Illustrator, Photoshop) aimed at forwarding Walt Disney planning initiatives.
    - Used GIS to analyze and manipulate LIDAR data to conduct visibility analysis on Walt Disney World property and new developments. 
    - Accompanied 3rd party drone flights that were conducted for planning purposes
    - Developed and maintained a geospatial database concerned with property-wide geotechnical reports.

    """)

    st.subheader("GIS Internship, Syracuse Community Geography")
    st.write("Dates: 2017 - 2018")
    st.write("Industry & Sector: Education, Private")
    st.write("Technologies: ArcGIS Pro, ArcMap, ArcGIS Online, ArcCollector, QGIS")
    st.write("""
             
    Responsibilities/Accomplishments:
             
    - In charge of conducting GIS projects for community organizations, aiding local companies to write proposals to the city for geographic purposes, studying and analyzing underground infrastructure using GIS tools.
    - Used ArcMap and ArcGIS online to create a series of Trail Maps using local GIS data and ArcGIS StoryMap templates.
    - Used ArcCollector to develop and maintain a geospatial database concerned with ADA curb cuts in the City of Syracuse 
             
    """)

elif page_selection == "Skills and Competencies":
    
    st.title("Skills and Competencies")
    st.subheader("Programming & Development")
    st.markdown(
    """
    **Languages & Libraries**
    - Python | Proficiency (10+ years experience)
        -   Pandas, GeoPandas, Pydantic, Plotly, Seaborn, Matplotlib, scikit-learn, TensorFlow, HuggingFace, Ollama, PySpark, requests,
            FastAPI, Flask, Streamlit, Dash, Arcpy, Transformers, LangChain, GDAL, Rasterio, Shapely, Fiona, OSMNX, Telethon, Selenium, BeautifulSoup, 
            Requests, Boto3, Click, Pytest, geemap
    - SQL | Proficiency (10+ years experience)
        - PostGIS, T-SQL, PL/pgSQL, MySQL, AWS Athena, SQlite
    - R | Proficiency (3+ years experience)
        - ggplot2, dplyr, tidyr, sf, caret, randomForest, sp, shiny, leaflet, plotly
    - JavaScript | Proficiency (2-3 years experience)
        - Leaflet, Mapbox GL JS, D3.js, React, Node.js, Flask, JQuery
    - HTML | Proficiency (2-3 years experience)
        - Bootstrap, Materialize
    - CSS | Proficiency (2-3 years experience)
        - Tailwind CSS, Bulma
    - CLI | Proficiency (10+ years experience)
        - Bash, PowerShell, Warp

    **Tools & Platforms**
    - AWS S3/EC2/RDS, AWS EMR, Databricks, Temporal, Kubernetes, Docker, PostgreSQL

    **IDE's & Notebooks**
    - Visual Studio Code, PyCharm, JupyterLab, RStudio, Brackets, Notepad ++
    """
    )

    st.subheader("Geographic Information Systems, Computing, LiDAR + Photogrammetry ")
    st.markdown(
    """
    - ArcGIS Pro, ArcMap, ArcGIS Online, ArcGIS StoryMaps, ArcGIS Web Map Developer, QGIS, AutoCAD Civil 3D, Agisoft Metashape, Pix4D, Mapbox SDK's, Autodesk ReCap, LIDAR360, ERDAS Imagine, PostGIS, GeoServer, Geoserver
    """
    )
    st.subheader("sUAS Experience, Solutions, Piloting, Ventures")
    st.markdown(

    """ 
    **Tools & Software**
    - Pix4D (Capture / Mapper / React / Cloud) , Skyward, DroneBase, DJI GO, SUASMAN, Agisoft Metashape, Bently Context Capture, Emotion, Measure Ground Control (MGC)l DroneDeploy l Q Ground Control, Skyvector, B4UFly, Marzipano, Airmap, UCGS, KittyHawk, Scopito
    **AirFrame Experience**
    - DJI Mavic Air, DJI Mavic Pro, DJI Phantom 4 Pro, DJI Inspire I, Parrot ANAFI USA, SenseFly eBee X, WingtraOne, Skydio 2, Autel Evo II Pro, Yuneec H520
    """
    )
    st.subheader("CAD & Design")
    st.markdown(
    """    - AutoCAD Civil 3D, Adobe Illustrator, Adobe Photoshop, Figma
    """
    )
    st.subheader("Customer Relationship Management")
    st.markdown(
    """    - Salesforce Lightning Service, HubSpot, Zendesk
    """
    )
    st.subheader("Project & Product Management Software")
    st.markdown(
    """    - AHA, Jira, Confluence, Trello, Asana, Monday.com
    """
    )
    st.subheader("Soft")
    st.markdown(
    """    
    - Working with customers is my dopamine
    - Workaholic (In-Moderation) - WILL WORK UNTIL THE JOB IS DONE
    - Incredible Communication and Writing Skills
    - The ability to innovate quickly and creatively
    - Incredibly motivated and have the ability to MOTIVATE
    - Ideation leading to successful design and product development
    """
    )

elif page_selection == "Projects":

    st.title("Personal Development Projects")
    st.subheader("xyzeus & galm")
    st.subheader("412Analytics & Game Outcome Predictor")
    st.subheader("Paladino Market Analytics/Market Mole")
    st.subheader("SiteWatch")
    st.subheader("Real Time Electrical Asset Vulnerability Index (RTEAVI)")

    st.title("Professional Development Projects")
    st.subheader("Sandcrawler")
    st.subheader("POI Fusion Engine")

elif page_selection == "Programming & Development":

    st.write("See skills and competencies page or hit the Quick Link in the sidebar to reach my GitHub!")

elif page_selection == "Certifications, Achievements, & Spotlights":

    st.title("Certifications, Achievements, & Spotlights")
    st.subheader("Professional Spotlights")
    st.write("Fall 2022 Syracuse University Maxwell School Alumni Spotlight: I was featured in The Syracuse University’s Maxwell School Magazine (Fall 2023 Edition) for my successes in the geospatial industry. Click button below for digital article.")
    st.link_button(
    "Link to Article",
    url="https://www.maxwell.syr.edu/news/article/maxwell-alum-launches-dream-job-pairing-geography-drones-and-data-in-washington-dc",
    use_container_width=False,
    )
    st.subheader("Certifications")
    st.write("""
            
            FAA Part 107 Unammed UAS
            - Obtained my UAV FAA Part 107 License - Summer 2017

            USAF BUQ I/II - Basic sUAS Qualifications Level I & II
            - Successfully took and received my BUQ I & II Certs. The certs allow me to fly sUAS (upon successful approval) @ any installation in the world.

            Parrot ANAFI USA Ground School & Basic Flight Course
            - Was successfully admitted and received training on the new Parrot ANAFI USA Drone. The training was hosted by the Air Force Civil Engineering Center in San Antonio. Training was a critical step for for AFCEC sUAS Office. 

            Miller Mountain: Introduction to Web Programming for GIS Applications
            - This class was not only incredible, but it changed the course of my career. Certification of Achievement on LinkedIn Profile… 

            Graeme Browning: ArcPy for ArcGIS Pro Developers
            - For any GIS Professional, this course is absolutely vital to understand. Thanks for Graeme for an incredible course on ArcPy for Pro!
             
            """)

    st.subheader("Academic, Athletic, & Personal Achievements")
    st.write("""
            - ACC All-Academic Honor Roll 2014 - 2018
            - ACC Indoor and Outdoor Track and Field Team | Winter 2018/Spring 2018
            - Member of the 2015 NCAA D1 National Champion Cross Country Team
            - Boy Scouts of America: Eagle Scout - May 2014
             """)

elif page_selection == "Contact":

    st.title("Contact Me")

    st.subheader("Cell")
    st.write("304-376-9192")

    st.subheader("Email")
    st.write("andyjpaladino@gmail.com")