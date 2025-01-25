import { useEffect, useState } from 'react';
import axios from 'axios';
import { Typewriter } from "react-simple-typewriter";
import TextToSpeech from './textToSpeech';

export default function StartTestButton() {
    const [data, setData] = useState('Loading...');
    const [input, setInput] = useState('');

    const sendMessage = async () => {
        try {
            const response = await axios.post('http://localhost:8080/chat', {
                message: input,
            });
            setData(response.data.message);
        } catch (error) {
            if (axios.isAxiosError(error)) {
                console.error('Error fetching data:', error.response?.data);
            } else {
                console.error('Error fetching data:', error);
            }
        }
    };

    return (
        <div className="flex flex-col items-center justify-center h-screen w-7/10">
            <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type your message here..."
                className="w-full p-2 border border-gray-300 rounded"
            />
            <button onClick={sendMessage} className="mt-2 p-2 bg-blue-500 text-white rounded">
                Send
            </button>
            <div className="mt-4">
                <Typewriter
                    words={[data]}
                    typeSpeed={50}
                    deleteSpeed={30}
                />
                {data}
            </div>
            <TextToSpeech/>
            
        </div>
    );
}
