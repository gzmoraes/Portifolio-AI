with open("sampleAiConfig.md", "r", encoding="utf-8") as file:
    sys_config = file.read()
    

config_variables = {
    "assist_name": "Atlas",
    "assist_persona": "friendly and professional.",
    
    "func_dict": {
        "about": "User wants to learn more about, his background, experience, or general information.",
        "contact": "User wants to get in touch, ask for contact details, or reach.",
        "projects": "User wants to see, learn about, or explore projects.",
        "services": "User inquires about offerings, services.",
        "skills": "User wants to know about technical abilities, programming languages, frameworks, or tools.",
        "socialMedia": "User asks for social media links, profiles, or ways to connect on social platforms.",
        "feedback": "User asks for feedback, reviews, or what others say about."
    },
    
    "portf_name": "Gabriel Tazz",
    "portf_role": "Full Stack Developer",
    "portf_about": "Passionate about programming.",
    "portf_location": "São Paulo, Brazil",
    "portf_expertise": "AI integration, Algorithm, Data Manipulation, Mechatronics",
    "portf_languages": "English, Portuguese",
    "portf_github": "github.com/GTazz",
    "portf_linkedin": "linkedin.com/in/gabriel-tazz",
    "portf_site": "gtazz.dev",
    "portf_graduation": "Bachelor's in Computer science and Mechatronics Engineering technition",
    "portf_skills": "Python, JavaScript, C++, HTML, CSS, React, Node.js, SQL"
}   

for K, V in config_variables.items():
    sys_config = sys_config.replace(f"<{K}>", str(V))

with open("aiConfig.md", "w", encoding="utf-8") as file:
    file.write(sys_config)
