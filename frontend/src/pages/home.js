import React from "react";
import  { Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import Login from "./login"
import Signup from "./signup"


const Home = () => {
    const [ hasAccount, setHasAccount ] = useState(false);
    const [loggedIn, setLoggedIn] = useState(false);
    const handleSignin = () => {}
    

    return (
        <div class="homepage">
            <div class="homepage-content">
                <h1>Deep Fake Detective</h1>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In gravida ornare imperdiet. Nam eget arcu id libero vulputate convallis.</p>
            </div>
            <div class="homepage-form">
                {hasAccount ? <Login /> : <Signup />}
            </div>
        </div>
    );
}

export default Home;