



// src/App.jsx

import React, { useState } from 'react';
import Header from './components/Header';
import NameForm from './components/NameForm';
import ResultsDisplay from './components/ResultsDisplay';

function App() {
  // ... (aapki saari state waise hi rahegi)
  const [name, setName] = useState('');
  const [hobby, setHobby] = useState('');
  const [customHobby, setCustomHobby] = useState('');
  const [type, setType] = useState('');
  const [special, setSpecial] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [generatedNames, setGeneratedNames] = useState([]);

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setGeneratedNames([]);

    const finalHobby = hobby === 'Other' ? customHobby : hobby;

    // --- YEH HAI SABSE ZAROORI LINE ---
    // Yeh Netlify se VITE_API_URL lega. Agar nahi mila, to local wala use karega.
    const apiUrl = import.meta.env.VITE_API_URL;

    try {
      // Hum yahaan 'apiUrl' ka istemal kar rahe hain
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: name,
          hobby: finalHobby,
          special: special,
          nameType: type,
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setGeneratedNames(data.generated_names || []);

    } catch (error) {
      console.error("Error fetching data:", error);
      alert("Oops! Kuch gadbad ho gayi. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center p-4 sm:p-8 font-sans">
      <div className="w-full max-w-2xl">
        <Header />
        <main className="mt-8">
          <NameForm
            name={name} setName={setName}
            hobby={hobby} setHobby={setHobby}
            customHobby={customHobby} setCustomHobby={setCustomHobby}
            type={type} setType={setType}
            special={special} setSpecial={setSpecial}
            isLoading={isLoading}
            handleFormSubmit={handleFormSubmit}
          />
          <ResultsDisplay 
            isLoading={isLoading} 
            generatedNames={generatedNames} 
          />
        </main>
      </div>
    </div>
  );
}

export default App;
