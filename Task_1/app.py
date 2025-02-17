from flask import Flask, render_template

app = Flask(__name__)

# Sample data for projects and blog posts
projects = [
    {
        "title": "Registration Form",
        "description": "A HTML,CSS and JavaScript based Registration form with the excption handling mechanisms",
        "live_demo": "https://jeevab700.github.io/RegistrationForm/",
        "github": "https://github.com/JeevaB700/RegistrationForm"
    },
    {
        "title": "To-Do List",
        "description": "A HTML,CSS and JavaScript based To-Do List with the basic functionality.",
        "live_demo": "https://jeevab700.github.io/Brainwave_Matrix_Intern/Task_1/",
        "github": "https://github.com/JeevaB700/Brainwave_Matrix_Intern/tree/main/Task_1"
    },
    # Add more projects as needed
        {
        "title": "E-Commerce Web Application",
        "description": "A Basic E-Commerce web application built using HTM,CSS and JavaScript.",
        "live_demo": "https://jeevab700.github.io/Brainwave_Matrix_Intern/Task_2/",
        "github": "https://github.com/JeevaB700/Brainwave_Matrix_Intern/tree/main/Task_2"
    },

]

blog_posts = [
    {
        "title": "My First Blog Post",
        "content": "This is the content of my first blog post.",
        "date": "2024-10-20"
    },
    {
        "title": "Learning Flask",
        "content": "In this post, I share my experiences while learning Flask.",
        "date": "2024-10-19"
    },
        {
        "title": "Learning Flask",
        "content": "In this post, I share my experiences while learning Flask.",
        "date": "2024-10-19"
    },

    # Add more blog posts as needed
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, blog_posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)