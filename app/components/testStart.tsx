import { useEffect, useState } from 'react';
import axios from 'axios';

export default function TestStart() {

    const fetchData = async () => {
        try {
            const response = await axios.get('http://localhost:8080/startScramble');
        } catch (error) {
            console.error('Error fetching data:', error);
        }
        

    };

    return (
        <div>
            <button onClick={fetchData}>Start</button>
        </div>
    );

}