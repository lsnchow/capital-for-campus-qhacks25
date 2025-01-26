"use client"
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Image, { StaticImageData } from 'next/image';
import homepageImage from '@/public/homepage.png';
import pixelLabel0 from '@/public/pixil-layer-0.png';
import pixelLabel1 from '@/public/pixil-layer-1.png';
import pixelLabel2 from '@/public/pixil-layer-2.png';
import pixelLabel3 from '@/public/pixil-layer-3.png';
import pixelLabel4 from '@/public/pixil-layer-4.png';
import pixelLabel5 from '@/public/pixil-layer-5.png';
import pixelLabel6 from '@/public/pixil-layer-6.png';



export default function Game() {
    const [sceneImageNum, setSceneImageNum] = useState(0);
    const [sceneImage, setSceneImage] = useState(homepageImage);
    const [score, setScore] = useState(1);
    const [blurb, setBlurb] = useState("Generating...");
    const [option1, setOption1] = useState("Generating...");
    const [option2, setOption2] = useState("Generating...");
    const [answer1, setAnswer1] = useState("Generating...");
    const [answer2, setAnswer2] = useState("Generating...");
    const [userAns, setUserAns] = useState("");
    const [results1, setResults1] = useState("");
    const [results2, setResults2] = useState("");
    const [isVisible, setVisible] = useState(false);
    const [bar, setBar] = useState(pixelLabel0);
    const [input, setInput] = useState("");
    
    const exportData = async () => {
        try {
            await axios.post('http://localhost:8080/output', {input});
        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        axios.get('http://localhost:8080/background')
            .then(response => {
                const dataArray = response.data;
                setSceneImage(dataArray[sceneImageNum] as StaticImageData);
                console.log("Success");
                console.log(dataArray[sceneImageNum]);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, [sceneImageNum]);

    useEffect(() => {
        axios.get('http://localhost:8080/content')
            .then(response => {
                const blurbArray = response.data;
                setBlurb(blurbArray[sceneImageNum * 5]);
                if (sceneImageNum === 0) {
                    setScore(0);
                }

                
                setOption1(blurbArray[sceneImageNum * 5 + 1]);
                setAnswer1(blurbArray[sceneImageNum * 5 + 2]);
                setOption2(blurbArray[sceneImageNum * 5 + 3]);
                setAnswer2(blurbArray[sceneImageNum * 5 + 4]);
                setResults2(blurbArray[35 + sceneImageNum]);
                setResults1(blurbArray[36 + sceneImageNum]);
                if (sceneImageNum === 0) {
                    setBar(pixelLabel0);
                } else if (sceneImageNum === 1) {
                    setBar(pixelLabel1);
                } else if (sceneImageNum === 2) {
                    setBar(pixelLabel2);
                } else if (sceneImageNum === 3) {
                    setBar(pixelLabel3);
                } else if (sceneImageNum === 4) {
                    setBar(pixelLabel4);
                } else if (sceneImageNum === 5) {
                    setBar(pixelLabel5);
                } else if (sceneImageNum === 6) {
                    setBar(pixelLabel6);
                }
                

                
                if(sceneImageNum === 6) {
                    if(score >= 8)
                    {
                        window.location.href = "http://localhost:3000/congratulations";
                        exportData();
                    }
                    else{
                        window.location.href = "http://localhost:3000/schooled";
                        exportData();
                    }
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, [sceneImageNum]);

    const handleOption1Click = () => {
        setUserAns(answer1);
        console.log(results1);
        setScore(score + Number(results1));
        console.log("results"+results1);
        setInput(input + "a" + Math.abs(Number(results1)).toString());
        setVisible(true);
        if (score <= 0) 
            {
                window.location.href = "http://localhost:3000/congratulations";
                exportData();
            }
    };

    const handleOption2Click = () => {
        setUserAns(answer2);

        console.log(results1);
        setScore(score + Number(results2));
        console.log("results"+results2);
        setInput(input + "b" + Math.abs(Number(results2)).toString());
        setVisible(true);
        if (score <= 0) 
            {
                window.location.href = "http://localhost:3000/congratulations";
                exportData();
            }
    };

    

    return (
        <div className="relative min-h-screen">
            <div className="fixed inset-0 -z-10">
                <Image
                    src={sceneImage}
                    alt="Background Image"
                    fill
                    className="object-cover"
                    priority
                />
            </div>
            <div style={{
                width: '1200px',
                height: '150px',
                borderRadius: '10px',
                backgroundColor: 'white',
                margin: '20px auto',
                padding: '20px',
                position: 'absolute',
                top: '0',
                left: '50%',
                transform: 'translateX(-50%)'
            }}>
                <div>{blurb}</div>
                
            </div>

            <div style={{
                width: '130px',
                height: '30px',
                position: 'fixed',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                zIndex: 9
            }}>
                <Image
                    src={bar}
                    alt="Progress Bar"
                    fill
                    className="object-cover"
                    priority
                />
            </div>
            
            

            <div style={{
                width: '800px',
                height: '350px',
                borderRadius: '10px',
                backgroundColor: 'white',
                margin: '20px auto',
                padding: '20px',
                position: 'absolute',
                bottom: '0',
                left: '50%',
                transform: 'translateX(-50%)',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                alignItems: 'center'
            }}>
                <button
                    style={{
                        width: '100%',
                        padding: '10px',
                        transition: 'background-color 0.3s ease',
                        borderRadius: '10px'
                    }}
                    onMouseEnter={(e) => e.currentTarget.style.backgroundColor = 'grey'}
                    onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'white'}
                    onClick={handleOption1Click}
                >
                    {option1}
                </button>

                <button
                    style={{
                        width: '100%',
                        padding: '10px',
                        transition: 'background-color 0.3s ease',
                        borderRadius: '10px'
                    }}
                    onMouseEnter={(e) => e.currentTarget.style.backgroundColor = 'grey'}
                    onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'white'}
                    onClick={handleOption2Click}
                >
                    {option2}
                </button>
                <div style={{
                    width: '100%',
                    padding: '10px',
                    transition: 'background-color 0.3s ease',
                    borderRadius: '10px',
                    display: 'flex',
                    flexDirection: 'column',
                }}
                >
                    {userAns}
                     User Score:
                    {score}
                    {isVisible && (
                    <button
                        style={{
                            width: '100%',
                            padding: '10px',
                            transition: 'background-color 0.3s ease',
                            borderRadius: '10px',
                            backgroundColor: 'lightblue',
                            marginTop: '10px'
                        }}
                        onClick={() => {
                            setSceneImageNum(sceneImageNum + 1);
                            setVisible(false); // Reset score when changing scene
                        }}
                    >
                        Next Scene
                    </button>
                )}
                </div>
                

            </div>
        </div>
    );
}


