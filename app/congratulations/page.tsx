"use client"

import { useState, useEffect } from 'react';
import axios from 'axios';
import { TypeAnimation } from 'react-type-animation';

export default function Textbox() {
    const [data, setData] = useState<string>('');
    const [blurbList, setBlurbList] = useState<string[]>([]);

    useEffect(() => {
        axios.get('http://localhost:8080/getResults')
            .then(response => {
                const dataInput = response.data;  // Access the correct key
                const formattedData = dataInput.split('');
                setData(dataInput)
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    useEffect(() => {
        axios.get('http://localhost:8080/content')
            .then(response => {
                const blurbArray = response.data;
                const output: string[] = [];
                for (let i = 0; i < 7; i++) {
                    if (data[i] === "a") {
                        output[i] = blurbArray[i * 5 + 2];
                    } else {
                        output[i] = blurbArray[i * 5 + 3];
                    }
                }
                setBlurbList(output);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, [data]);

    return (
        <div>
            <div className="flex flex-row bg-black min-h-screen">
                <div className="fixed ml-[300px] mt-[200px] flex flex-col items-center gap-4">
                    <div className="w-[400px] h-[400px]">
                        <img
                            src="/average-apple-math-kid.png"
                            alt="average apple math kid"
                            className="w-full h-full object-contain"
                        />
                    </div>
                    <div className="w-[400px] min-h-[100px]">
                        <TypeAnimation
                            sequence={["Congratulations! You win! You should start a portfolio:)"]} 
                            wrapper="div"
                            speed={50}
                            repeat={0}
                            cursor={false}
                            style={{ color: 'white' }}
                        />
                    </div>
                    
                </div>
                <div className="flex-1">
                <div className="fixed right-[300px] mt-[200px] flex flex-col items-center gap-4">
                    <div className="w-[400px] h-[400px]">
                        {blurbList.map((blurb, index) => (
                            <p key={index} className={data[7 + index] === "2" ? "text-green-500" : "text-red-500"}>
                                {blurb}
                            </p>
                        ))}
                    </div>
                </div>
                </div>
            </div>
        </div>
    )
}
