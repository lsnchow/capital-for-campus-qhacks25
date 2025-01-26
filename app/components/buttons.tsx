import { useState,useEffect } from 'react';
import axios from 'axios';

export default function Buttons() {
    
    const sendMessage = async () => {
        
    };
    return (
        <div className="flex flex-col space-y-4 p-10">
            <button 
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded transition duration-300 text-lg" onClick={sendMessage}
            >
                Start
            </button>
        </div>
    );
}