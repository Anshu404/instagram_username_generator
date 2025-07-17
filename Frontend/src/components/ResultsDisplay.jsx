// src/components/ResultsDisplay.jsx

import React from 'react';

// Yeh component do props accept karta hai:
// isLoading: agar true ho, toh loading animation dikhani hai
// generatedNames: yeh ek array hai jisme AI se aaye huye usernames honge
function ResultsDisplay({ isLoading, generatedNames }) {

  // Username ko clipboard mein copy karne wali function
  const handleCopy = (name) => {
    navigator.clipboard.writeText(name); // Clipboard API ka use karke copy karna
    alert(`Copied "${name}" to clipboard!`); // Confirmation alert
  };

  // Agar loading ho rahi hai toh spinner (ghoomti hui animation) aur message dikhao
  if (isLoading) {
    return (
      <div className="mt-10 text-center">
        {/* Spinner */}
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-pink-500 mx-auto"></div>
        
        {/* Loading Message */}
        <p className="mt-4 text-lg text-gray-300">Aapke liye Gen-Z names dhoondh rahe hain...</p>
      </div>
    );
  }

  // Agar abhi tak names generate nahi hue ya array empty hai, toh kuch mat dikhao
  if (!generatedNames || generatedNames.length === 0) {
    return null;
  }

  // Jab AI se usernames mil jaayein, tab unhe ek box mein list form mein display karo
  return (
    <div className="mt-10 w-full p-6 bg-gray-800 rounded-xl border border-gray-700">
      {/* Heading */}
      <h2 className="text-2xl font-bold text-center text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-500 mb-6">
        Aapke Liye Kuch Usernames!
      </h2>

      {/* List of generated usernames */}
      <div className="space-y-3">
        {generatedNames.map((name, index) => (
          <div 
            key={index} 
            className="flex justify-between items-center p-4 bg-gray-700 rounded-lg transition-transform hover:scale-105"
          >
            {/* Username Text */}
            <p className="font-mono text-lg text-white">{name}</p>

            {/* Copy Button */}
            <button
              onClick={() => handleCopy(name)}
              className="px-3 py-1 text-sm bg-pink-500 text-white rounded-md hover:bg-pink-600 transition"
            >
              Copy
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ResultsDisplay;
