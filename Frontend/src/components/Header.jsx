import React from 'react';

// Yeh component sirf app ka title dikhayega.
function Header() {
  return (
    <div className="text-center">
      <h1 className="text-4xl md:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600">
        Username Generator
      </h1>
      <p className="text-gray-400 mt-2">
        Apni personality se ek unique Instagram username banayein!
      </p>
    </div>
  );
}

export default Header;
