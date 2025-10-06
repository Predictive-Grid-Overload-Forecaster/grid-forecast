import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import "./css/Navbar/navbar.css";

const Navbar = () => {
    const [show, setShow] = useState(false);

    return (
        <div className="navbar">
            {!show && (
                <button className="hamburger-btn" onClick={() => setShow(true)}>☰</button>
            )}

            {show && (
                <div className={`sidebar ${show ? "open" : ""}`}>
                    <div className="top-line-navbar">     
                        <button className="close-btn" onClick={() => setShow(!show)}>☰</button>   
                        <h2 className="logo">GridWise</h2>
                    </div>

                    <nav className="nav-links">
                        <NavLink onClick={() => {setShow(!show)}} to="/" className="link">Dashboard</NavLink>
                        <NavLink onClick={() => {setShow(!show)}} to="/Energy_map" className="link">Energy Map</NavLink>
                        <NavLink onClick={() => {setShow(!show)}} to="/Renewables" className="link">Renewables</NavLink>
                        <NavLink onClick={() => {setShow(!show)}} to="/Chatbot" className="link">Chat Bot</NavLink>
                        <NavLink onClick={() => {setShow(!show)}} to="/Alerts" className="link">Alerts</NavLink>
                        <NavLink onClick={() => {setShow(!show)}} to="/Help" className="link">Help & Support</NavLink>
                    </nav>
                </div>
            )}
        </div>
    );
};

export default Navbar;
