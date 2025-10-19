import React, { useState } from "react";
import './css/Chatbot/chatbot.css'

const Chatbot = () => {
    const [response, setResponse] = useState("");
    const [question, setQuestion] = useState("");
    const [color, setColor] = useState("red");
    const [Disabledtbn, SetDisabledbtn] = useState(true);

    const [Question, Setquestion] = useState([])

    const handleChange = (e) => {
        const value = e.target.value;
        setQuestion(value);
        if (value.trim() === "") {
            setColor("red");
            SetDisabledbtn(true);
        } else {
            setColor("white");
            SetDisabledbtn(false);
        }
    };

    const ontap = () => {
    };

    return (
        <div className="chatbot-container">
            <h2 className="chatbot-title">Hi, You can Ask Here</h2>
            <div className="chatbot-response">{response}</div>
            <div className="chatbot-input-group">
                <input
                    className="chatbot-input"
                    value={question}
                    onChange={handleChange}
                />
                <button
                    className={`chatbot-button ${color === "red" ? "btn-red" : "btn-white"}`}
                    disabled={Disabledtbn}
                    onClick={ontap}
                >Ask</button>
            </div>
        </div>
    );
};

export default Chatbot;
