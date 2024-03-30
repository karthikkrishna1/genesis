import React, { useState } from "react";
import axios from "axios";

export default function Signup() {
    const [username, setUserName] = useState();
    const [password, setPassword] = useState();

    const handleSubmit = async e => {
        e.preventDefault();
        const login_payload = {
            username,
            password
        }
        axios.post(
            "http://localhost:5000/login", // Make a login endpoint
            login_payload
        ).then(response => {
            const token = response.data.access_token;
            localStorage.setItem("token", token);
            console.log(token);
            // setAuthToken(token);
            window.location.href = '/docs'
        }).catch(err => console.log(err));
    };

    return (
        <div className="signupform">
            <h1 class="title">
                Sign up Now!
            </h1>
            <div className="signup-wrapper">
                <form onSubmit={handleSubmit}>
                    <div className="signupcontainer">
                        <label for="Full Name">Full Name</label>
                        <input id="Full Name" type="text" className="Full Name" name="name" placeholder="E.g 'j.smith'"  maxlength="20" required onChange={e => setUserName(e.target.value)} />
                        <label for="username">Email or Username:</label>
                        <input id="username" type="text" className="username" name="name" placeholder="E.g 'j.smith'"  maxlength="20" required onChange={e => setUserName(e.target.value)} />
                        <label for="pword">Password:</label>
                        <input id="username" type="password" className="pword" name="name"  maxlength="20" required onChange={e => setPassword(e.target.value)}/>
                        <label for="pword">Confirm Password:</label>
                        <input id="username" type="password" className="pword" name="name"  maxlength="20" required onChange={e => setPassword(e.target.value)}/>
                    </div>
                    <div className="button-container">
                        <button class="button" type="submit">
                            Sign Up
                        </button>
                        <button class="button" type="submit">
                            Back to Login
                        </button>
                    </div>
                </form>
            </div>
        </div>
    )
}