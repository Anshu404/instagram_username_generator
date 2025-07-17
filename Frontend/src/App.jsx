// src/App.jsx

import React, { useState } from 'react';
import Header from './components/Header';
import NameForm from './components/NameForm';
import ResultsDisplay from './components/ResultsDisplay'; // Naye component ko import karo

function App() {
  // Saari state ab 'App' component ke paas rahegi
  const [name, setName] = useState('');
  const [hobby, setHobby] = useState('');
  const [customHobby, setCustomHobby] = useState('');
  const [type, setType] = useState(''); // Naya 'nameType' ke liye state
  const [special, setSpecial] = useState('');
  
  const [isLoading, setIsLoading] = useState(false);
  const [generatedNames, setGeneratedNames] = useState([]); // Results ko array mein store karenge

  // Form submit ka poora logic ab yahaan hai
  const handleFormSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setGeneratedNames([]); // Purane results ko saaf karo

    const finalHobby = hobby === 'Other' ? customHobby : hobby;

    try {
      const response = await fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: name,
          hobby: finalHobby,
          special: special,
          nameType: type, // 'nameType' ko backend mein bhejo
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setGeneratedNames(data.generated_names || []); // State ko naye names se update karo

    } catch (error) {
      console.error("Error fetching data:", error);
      // Aap yahaan ek error message bhi state mein set karke dikha sakte hain
      alert("Oops! Kuch gadbad ho gayi. Please try again.");
    } finally {
      setIsLoading(false); // Loading ko band karo
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
            type={type} setType={setType} // type aur setType ko props mein bhejo
            special={special} setSpecial={setSpecial}
            isLoading={isLoading}
            handleFormSubmit={handleFormSubmit} // Submit logic ko prop mein bhejo
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