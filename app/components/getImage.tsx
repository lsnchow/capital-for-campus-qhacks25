import { useEffect, useState } from 'react';
import axios from 'axios';

export default function GetImage() {
    const [imageURL, setImageURL] = useState('Loading...');

    useEffect(() => {
        console.log("Fetching image...");
        axios.get('http://localhost:8080/imageA')
            .then(response => {
                console.log("Response received:", response);
                setImageURL(response.data.message);  // Access the correct key
                console.log(imageURL);
                console.log("right here");
                console.log(response.data.message);  // Log the correct key
            })
            .catch(error => {
                console.log("HELPPP");
                console.error('Error fetching data:', error.response.data);
            });
    }, []);

    return (
        <div className="flex flex-col items-center justify-center h-screen w-7/10">
            <img src={imageURL} alt="Description of the fetched content" className="max-w-full h-auto" />
        </div>
    );
}
