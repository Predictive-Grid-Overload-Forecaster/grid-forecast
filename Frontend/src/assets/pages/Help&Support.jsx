import React, { useState } from "react";
import './css/Help/help.css'
import help_glowing_logo from './css/logo/help_glowing_logo.png';

const Help = () => {
    const help_data = [
        { logo: "🗺️", title: "Using the Energy Map", text: "Visualize real-time grid load and identify potential overload areas with our interactive map" },
        { logo: "📈", title: "Interpreting Renewable View", text: "Set up and customize notification for Critical, Warning and Stable Grid conditions." },
        { logo: "🎯", title: "Managing Alerts", text: "Set up and customize notification for Critical, Warning and Stable Grid conditions." }
    ];

    const question_data = [
        { question: "How is the Grid Overload Forecast Calculated ?", answer: "Yes, you can export historical data and forecast reports in CSV or PDF format from the 'Reports' section in your settings. This allows for offline analysis and integration with other systems." },
        { question: "Can I export data from the dashboard ?", answer: "Yes, you can export historical data and forecast reports in CSV or PDF format from the 'Reports' section in your settings. This allows for offline analysis and integration with other systems." },
        { question: "How often is the data refreshed ?", answer: "Real-time data on the dashboard is refreshed every 5 minutes. The predictive forecast models are updated every hour to provide you with the most current and reliable information for grid management" }
    ];

    const [showquestion, setShowquestion] = useState(question_data.map(() => false));

    const toggleFaq = (index) => {
        const newState = [...showquestion];
        newState[index] = !newState[index];
        setShowquestion(newState);
    };

    return (
        <div className="help-container">

            <div className="help-header">
                <div className="help-logo-title">
                    <img src={help_glowing_logo} alt="Help Glowing Logo" className="help-logo" />
                    <h2 className="help-title">Need Help?</h2>
                </div>
                <p className="help-subtitle">Find answers and get support for the Energy Grid Dashboard</p>
            </div>

            <div className="help-search">
                <input placeholder="🔍 Type to Find topic instantly" type="text" className="help-search-input" />
            </div>

            <div className="help-quick-guide">
                <h2 className="section-title">Quick Guide</h2>
                <div className="quick-guide-items">
                    {help_data.map((data, i) => (
                        <div key={i} className="guide-item">
                            <p className="guide-icon">{data.logo}</p>
                            <h3 className="guide-title">{data.title}</h3>
                            <p className="guide-text">{data.text}</p>
                            <button className="guide-btn">Learn more</button>
                        </div>
                    ))}
                </div>
            </div>

            <div className="help-faq">
                <h2 className="section-title">Frequently Asked Questions</h2>
                {question_data.map((data, i) => (
                    <div key={i} className="faq-item">
                        <p className="faq-question">{data.question}</p>
                        <button className="faq-toggle" onClick={() => toggleFaq(i)}>
                            {showquestion[i] ? "-" : "+"}
                        </button>
                        {showquestion[i] && (
                            <div className="answer">
                                <p>{data.answer}</p>
                            </div>
                        )}
                    </div>
                ))}
            </div>

            <div className="help-contact">
                <h3 className="contact-title">Can't find What You're looking for ?</h3>
                <p className="contact-text">You can mail us we will contact you asap</p>
                <button className="contact-btn">Contact Support</button>
            </div>

        </div>
    );
};

export default Help;
