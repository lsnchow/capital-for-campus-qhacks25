"use client"
import { useEffect, useState } from "react"
import axios from 'axios';
export default function Textbox () {
  const [data, setData] = useState('Loading...');
  useEffect(() => {
    axios.get('http://localhost:8080/')
    .then(response => {
      setData(response.data.message);  // Access the correct key
      console.log(data);
      console.log(response.data.message);  // Log the correct key
    })
    .catch(error => {
      console.log("HELPPP");
      console.error('Error fetching data:', error.response.data);
    });
  }, []);
  

  return (
    <div className="flex flex-col items-center justify-center h-screen" style={{ width: '70%' }}>
      {data}
    </div>
  )
}