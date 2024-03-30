import { React, useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes, Switch } from "react-router-dom";
import axios from "axios";
import {format} from "date-fns";
import './App.css';
import Home from "./pages/home";
import Login from "./pages/login";

const baseUrl = "http://localhost:5000";

function App() {

  const [description, setDescription] = useState("");
  const [eventsList, setEventsList] = useState([]);

  const fetchEvents = async () => {
    const data = await axios.get(`${baseUrl}/events`);
    const { events } = data.data;
    setEventsList(events);
  }

  useEffect(() => {
    fetchEvents();
  }
  , []);

  const handleChange = (e) => {
    setDescription(e.target.value)
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await axios.post(`${baseUrl}/events`, {description});
      setEventsList([...eventsList, data.data]);
      setDescription("");
    } catch (err) {
      console.log(err.message)
    }
  }

  return (
    <div className="App">
        <Router>
          <Routes>
            <Route exact path="/" element={<Home />} />
            {/* <Route exact path="/call" element={<Call />} /> */}
          </Routes>
        </Router>
    </div>
  );
}

export default App;
