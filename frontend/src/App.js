import axios from "axios";
import {format} from "date-fns";
import { useState, useEffect } from "react";
import './App.css';

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
        <form onSubmit={handleSubmit}>
          <label htmlFor="description">Description</label>
          <input
            onChange={handleChange}
            type="text"
            name="description"
            id="description"
            value={description}
          />
          <button type="submit">Submit</button>
        </form>
    </div>
  );
}

export default App;
