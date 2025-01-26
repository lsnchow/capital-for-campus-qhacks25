"use client"


import LandingPage from './components/landingPage'
import Image from 'next/image'

export default function Home() {
  return (
    <div className="relative min-h-screen">
      <div className="fixed inset-0 -z-10">
        <Image
          src="/homepage.png"
          alt="Background Image"
          fill
          className="object-cover"
          priority
        />
      </div>
      <div>
        <LandingPage />
      </div>
    </div>
  )
}