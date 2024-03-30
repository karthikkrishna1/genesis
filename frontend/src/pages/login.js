import React, { useState } from "react";
import axios from "axios";
import { setAuthToken } from "../utils/auth";

export default function Login() {
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
            setAuthToken(token);
            window.location.href = '/docs'
        }).catch(err => console.log(err));
    };

    return (
        <div className="loginform">
            <h1 class="title">
                Welcome Back!
            </h1>
            <div className="login-wrapper">
                <form onSubmit={handleSubmit}>
                    <div className="logincontainer">
                        <label for="username">Email or Username:</label>
                        <input id="username" type="text" className="username" name="name" placeholder="E.g 'j.smith'"  maxlength="20" required onChange={e => setUserName(e.target.value)} />
                        <label for="pword">Password:</label>
                        <input id="username" type="password" className="pword" name="name"  maxlength="20" required onChange={e => setPassword(e.target.value)}/>
                        <a class="forgotpword" href="/">Forgot Password?</a>
                    </div>
                    <button class="button" type="submit">
                        Login
                    </button>
                </form>
            </div>
        </div>
    )
}