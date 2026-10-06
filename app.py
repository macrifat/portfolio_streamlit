
/
















App · PY
from pathlib import Path
 
import streamlit as st
 
st.set_page_config(
    page_title="Monsur Ahmed Chowdhury | Test Automation Engineer",
    page_icon="🧪",
    layout="centered",
)
 
NAME = "Monsur Ahmed Chowdhury"
TITLE = "Automotive Software Test Engineer"
LOCATION = "Berlin, Germany"
EMAIL = "chowdhury93.tuc@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/monsur-ahmed-chowdhury-50948319b/"
GITHUB = "https://github.com/macrifat?tab=repositories"
 
SUMMARY = (
    "I test automotive infotainment and ADAS software for Mercedes-Benz at Luxoft/MBition. "
    "Over 4+ years I have built Python test automation, flashed ECUs on vehicles and test benches, "
    "and wired the results into CI/CD pipelines. I care about software quality, automation, "
    "and AI-assisted testing."
)
 
SKILLS = {
    "Programming": ["Python", "Java", "C++"],
    "Test automation": ["PyTest", "Robot Framework", "Selenium", "Postman", "REST API testing"],
    "DevOps / CI/CD": ["Git", "GitLab CI/CD", "Jenkins", "Docker"],
    "Automotive": ["CAN", "Ethernet", "DLT", "AUTOSAR", "ADAS", "QNX", "ECU flashing", "Diagnostics", "Monaco", "DLT Viewer"],
    "Web": ["Django", "REST API", "JavaScript", "Streamlit"],
    "AI": ["Generative AI with LLMs and RAG", "Agentic AI (beginner, with Claude)"],
    "Cloud": ["AWS (basic)", "Google Cloud (basic)"],
    "IoT": ["Raspberry Pi", "MQTT"],
    "Languages": ["English (advanced)", "German (B1)"],
}
 
EXPERIENCE = [
    {
        "role": "Test Engineer",
        "org": "Luxoft GmbH / MBition (Mercedes-Benz projects)",
        "place": "Berlin, Germany",
        "period": "June 2023 to present",
        "points": [
            "Design and execute system-level test cases for Mercedes-Benz infotainment and ADAS platforms.",
            "Run regression, performance, stress, and vehicle validation testing.",
            "Flash ECUs on vehicles and hardware test benches.",
            "Validate software builds before and after merge requests.",
            "Analyze CAN, Ethernet, and DLT logs to investigate issues.",
            "Develop Python automation frameworks for regression testing, reducing manual validation effort and improving test execution efficiency.",
            "Build automation pipelines for flashing and result analysis.",
            "Work with developers and stakeholders in Agile teams.",
        ],
        "tech": "Python, PyTest, Jenkins, GitLab, Docker, Monaco, DLT Viewer, CAN, Ethernet, QNX, AUTOSAR, ADAS",
    },
    {
        "role": "Software Developer",
        "org": "Livello Technologies",
        "place": "Düsseldorf, Germany",
        "period": "April 2022 to May 2023",
        "points": [
            "Developed Python software for Edge IoT applications.",
            "Designed an automated testing framework with PyTest and a Dockerized test environment.",
            "Supported CI/CD pipelines and continuous deployment.",
            "Verified bug fixes and software releases, and produced verification reports and quality metrics.",
        ],
        "tech": "Python, PyTest, Docker, CI/CD, MQTT",
    },
    {
        "role": "Working Student and Intern",
        "org": "Python software development and test automation",
        "place": "",
        "period": "",
        "points": [
            "Developed a payment system for smart kiosks.",
            "Integrated MQTT communication and supported the network agent.",
            "Wrote unit tests and automated tests in Python.",
        ],
        "tech": "Python, MQTT, unit testing",
    },
]
 
PROJECTS = [
    ("Regression automation framework",
     "Python-based framework for regression testing of Mercedes-Benz infotainment and ADAS platforms.",
     "Python, PyTest"),
    ("Flashing and result-analysis pipelines",
     "Automation pipelines that flash ECUs and analyze the results.",
     "Jenkins, GitLab CI/CD, Docker"),
    ("Edge IoT software testing for smart kiosks",
     "Master's thesis at the Technical University of Chemnitz.",
     "Python, MQTT, Edge IoT"),
    ("Smart kiosk payment system",
     "Payment system built during a working student role.",
     "Python, MQTT"),
    ("Generative AI, RAG, and agentic AI",
     "Learning project: retrieval-augmented generation and agentic workflows with Claude (beginner level).",
     "LLMs, RAG, Claude"),
]
 
EDUCATION = [
    ("Master's in Automotive Software Engineering",
     "Technical University of Chemnitz, Germany", "2019 to 2023",
     "Thesis: Edge IoT Software Testing for Smart Kiosk Solutions"),
    ("Bachelor's in Electrical and Electronic Engineering",
     "American International University Bangladesh, Dhaka", "2011 to 2015", ""),
]
 
CERTS = [
    "Robot Framework & Selenium with Python",
    "Agile & Scrum Project Management",
    "Generative AI / RAG",
]
 
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;700&display=swap');
    html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
    h1 { font-weight: 700; letter-spacing: -0.02em; }
    .chip { display:inline-block; padding:2px 10px; margin:0 6px 6px 0; border:1px solid #0E6E8C;
            border-radius:4px; font-size:0.85rem; color:#0E6E8C; }
    .meta { color:#5b6770; font-size:0.9rem; }
    .block-container { max-width: 56rem; padding-top: 2rem; }
    button[title="View fullscreen"] { display:none; }
    [data-testid="stImage"] img { max-width: 14rem !important; }
    .stats { display:flex; flex-wrap:wrap; gap:1.5rem 3rem; margin-top:1rem; }
    .stats div { min-width:9rem; }
    .stats .label { font-size:0.85rem; color:#5b6770; }
    .stats .value { font-size:1.25rem; font-weight:500; line-height:1.3; white-space:nowrap; }
    </style>
    """,
    unsafe_allow_html=True,
)
 
photo = Path(__file__).parent / "photo.jpg"
head_photo, head_text = st.columns([1, 2.4], vertical_alignment="center", gap="large")
with head_text:
    st.title(NAME)
    st.subheader(TITLE)
    st.markdown(f"<span class='meta'>{LOCATION}</span>", unsafe_allow_html=True)
if photo.exists():
    head_photo.image(str(photo), width=220)
 
c1, c2, c3, c4 = st.columns([1.05, 0.9, 1.05, 5], gap="small")
c1.link_button("LinkedIn", LINKEDIN)
c2.link_button("GitHub", GITHUB)
c3.link_button("Email me", f"mailto:{EMAIL}")
cv = Path(__file__).parent / "CV_Monsur_Chowdhury.pdf"
if cv.exists():
    c4.download_button("Download CV (PDF)", cv.read_bytes(), file_name=cv.name, mime="application/pdf")
 
tab_about, tab_exp, tab_proj, tab_skills, tab_edu = st.tabs(
    ["About", "Experience", "Projects", "Skills", "Education"]
)
 
with tab_about:
    st.write(SUMMARY)
    st.markdown(
        "<div class='stats'>"
        "<div><div class='label'>Years in test automation</div><div class='value'>4+</div></div>"
        "<div><div class='label'>Current client</div><div class='value'>Mercedes-Benz</div></div>"
        "<div><div class='label'>Languages</div><div class='value'>EN (advanced), DE (B1)</div></div>"
        "</div>",
        unsafe_allow_html=True,
    )
 
with tab_exp:
    for job in EXPERIENCE:
        with st.container(border=True):
            st.markdown(f"### {job['role']}")
            meta = " | ".join(x for x in [job["org"], job["place"], job["period"]] if x)
            st.markdown(f"<span class='meta'>{meta}</span>", unsafe_allow_html=True)
            for p in job["points"]:
                st.markdown(f"- {p}")
            st.caption(f"Technologies: {job['tech']}")
 
with tab_proj:
    cols = st.columns(2)
    for i, (title, desc, tech) in enumerate(PROJECTS):
        with cols[i % 2].container(border=True):
            st.markdown(f"**{title}**")
            st.write(desc)
            st.caption(tech)
    st.markdown(f"More code on [GitHub]({GITHUB}).")
 
with tab_skills:
    for group, items in SKILLS.items():
        st.markdown(f"**{group}**")
        st.markdown("".join(f"<span class='chip'>{s}</span>" for s in items), unsafe_allow_html=True)
    st.markdown("**Certifications and courses**")
    for c in CERTS:
        st.markdown(f"- {c}")
 
with tab_edu:
    for degree, school, years, extra in EDUCATION:
        with st.container(border=True):
            st.markdown(f"**{degree}**")
            st.markdown(f"<span class='meta'>{school} | {years}</span>", unsafe_allow_html=True)
            if extra:
                st.write(extra)
    st.markdown(f"Contact: [{EMAIL}](mailto:{EMAIL})")
 
