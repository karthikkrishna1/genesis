import React from "react";
import  { Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import Login from "./login"
import Signup from "./signup"


const Home = () => {
    const [ hasAccount, setHasAccount ] = useState(true);
    const [loggedIn, setLoggedIn] = useState(false);
    const handleSignin = () => {}
    

    return (
        <div class="homepage">
            <div class="homepage-content">
                <h1><b>WOKE</b></h1>
                <p>Harness the power of clarity in every conversation, ensuring your communications are authentically human.
                <br></br><br></br>
                <b>Secure conversations, authentic interactions</b> — experience the future of communication with Woke.</p>
            </div>
            <div class="homepage-form">
                <a href="/call">
                    <button class="animated-button">
                    <svg viewBox="0 0 24 24" class="arr-2" xmlns="http://www.w3.org/2000/svg">
                        <path
                        d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z"
                        ></path>
                    </svg>
                    <span class="text">Get Started</span>
                    <span class="circle"></span>
                    <svg viewBox="0 0 24 24" class="arr-1" xmlns="http://www.w3.org/2000/svg">
                        <path
                        d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z"
                        ></path>
                    </svg>
                    </button>
                </a>
            </div>
        </div>
    );
}

export default Home;