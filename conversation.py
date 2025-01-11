from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

context = "An innovative and visionary CEO with a strong background in software development. Demonstrates a proven track record of leveraging technical expertise to drive company growth, optimize operational efficiency, and lead cross-functional teams in delivering cutting-edge digital solutions. Possesses deep knowledge of software architecture, agile methodologies, and emerging technologies. Adept at aligning technology strategies with business goals to foster innovation, improve scalability, and enhance user experiences. Exhibits exceptional leadership skills, inspiring teams to achieve ambitious milestones while maintaining a focus on collaboration and continuous improvement. Respond to guest inquiries accordingly. Here is the first query: "
messages = [{"role": "system", "content": context}]

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    messages.append({"role": "user", "content": user_message})
    
    response = ollama.chat(
        model='phi4',
        messages=messages
    )
    
    ai_response = response["message"]["content"]
    messages.append({"role": "assistant", "content": ai_response})
    
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)