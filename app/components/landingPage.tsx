import Link from "next/link"
import Buttons from "./buttons"
import { TypeAnimation } from 'react-type-animation';
import { useEffect,useState } from "react";
import axios from 'axios';


export default function LandingPage() {
    
  useEffect(() => {
    axios.get('http://localhost:8080/api')
    .then(response => {
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
  }, []);
    return (
        <div className="relative z-10 flex flex-col items-center justify-center min-h-screen">
        <div className="relative">
          <div
            style={{ width: '450px', height: '400px', backgroundColor: 'white' }}
            className="rounded-lg"
          />
          <div
            style={{
              color: '#00324d',
              fontSize: '5rem',
              textAlign: 'center',
              textShadow: '2px 2px 4px #4b2e2e'
            }}
            className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
          >
            <TypeAnimation
                            sequence={["Campus to Capital"]}
                            wrapper="div"
                            speed={50}
                            repeat={0}
                            cursor={true}
                            style={{ color: 'white' }}
                        />
            
          </div>
        </div>
        <Link href="/game">
          <Buttons/>
        </Link>
      </div>
    )
}