"use client"

import GetImage from "./components/getImage"
import StartTestButton from "./components/startTest"
import TestStart from "./components/testStart"
import Textbox from "./components/textbox"

export default function Home () {

  

  return (
    <div className = "flex flex-col items-center justify-center h-screen">

      <Textbox/>   
      <TestStart/> 
      <StartTestButton/>
    </div>
  )
}

//<GetImage/>