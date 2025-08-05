


functions = {
    "about": "User wants to learn more about, his background, experience, or general information.",
    "contact": "User wants to get in touch, ask for contact details, or reach.",
    "projects": "User wants to see, learn about, or explore projects.",
    "services": "User inquires about offerings, services.",
    "skills": "User wants to know about technical abilities, programming languages, frameworks, or tools.",
    "socialMedia": "User asks for social media links, profiles, or ways to connect on social platforms.",
    "feedback": "User asks for feedback, reviews, or what others say about.",
}

tools = []
for func_name, func_description in functions.items():
    
    func_model = {
        "type": "function",
        "function": {
            "name": func_name,
            "description": func_description,
            "parameters": {
                "type": "object",
                "properties": {
                    "ai_response": {
                        "type": "string",
                        "description": "Text response to the user's message.",
                    }
                },
            },
        },
    }
    tools.append(func_model)

print(tools)