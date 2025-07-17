// src/components/NameForm.jsx

import React from 'react';

// Dekho, hum saare props ko yahaan le rahe hain, jisme 'type', 'setType', aur 'handleFormSubmit' bhi shamil hain
function NameForm({ 
  name, setName, 
  hobby, setHobby, 
  customHobby, setCustomHobby, 
  type, setType, // Naye props
  special, setSpecial, 
  isLoading, 
  handleFormSubmit // Naya prop
}) {
  
  const hobbyOptions = [
    "🎨 Art", "📚 Reading", "💻 Coding", "🎮 Gaming", "✈️ Traveling",
    "🍔 Foodie", "💪 Fitness", "🎵 Music", "Other"
  ];

  // Is component se local submit logic hata diya gaya hai.

  return (
    // Ab 'onSubmit' App.jsx se mile function ko call karega
    <form onSubmit={handleFormSubmit} className="space-y-6 bg-gray-800/50 p-8 rounded-xl border border-gray-700">
      
      {/* Name Input */}
      <div>
        <label htmlFor="name" className="block text-sm font-medium text-gray-300 mb-2">
          Aapka naam ya nickname?
        </label>
        <input
          id="name" type="text" value={name} onChange={(e) => setName(e.target.value)}
          placeholder="e.g., Anshu"
          className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-pink-500 outline-none transition"
          required
        />
      </div>

      {/* Hobby Selector */}
      <div>
        <label htmlFor="hobby" className="block text-sm font-medium text-gray-300 mb-2">
          Aapka main hobby kya hai?
        </label>
        <select
          id="hobby" value={hobby} onChange={(e) => setHobby(e.target.value)}
          className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-pink-500 outline-none transition"
          required
        >
          <option value="" disabled>Select a hobby</option>
          {hobbyOptions.map((opt) => (
            <option key={opt} value={opt}>{opt}</option>
          ))}
        </select>
      </div>

      {/* Custom Hobby Input (Conditional) */}
      {hobby === 'Other' && (
        <div>
          <label htmlFor="customHobby" className="block text-sm font-medium text-gray-300 mb-2">
            Apna hobby likhein:
          </label>
          <input
            id="customHobby" type="text" value={customHobby} onChange={(e) => setCustomHobby(e.target.value)}
            placeholder="e.g., Collecting stamps"
            className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-pink-500 outline-none transition"
            required
          />
        </div>
      )}

      {/* Name Type Selector */}
      <div>
        <label htmlFor="nameType" className="block text-sm font-medium text-gray-300 mb-2">
          Aapko kis vibe ka naam chahiye?
        </label>
        <select
          id="nameType" value={type} onChange={(e) => setType(e.target.value)}
          className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-pink-500 outline-none transition"
          required
        >
          <option value="" disabled>Select a name type</option>
          <option value="casual">Casual</option>
          <option value="brainrot">💥 Brainrot Mode ON</option>
          <option value="bimbo">💄 Bimbo but Make it Coded</option>
          <option value="rainbow">🌈 Rainbow Unicorn Vibes</option>
          <option value="desi">🧃 Desi Masala Vibes</option>
          <option value="sad">🖤 Sad but Slaying</option>
          <option value="darkacademia">🕯️ Dark Academia ft. Your Trauma</option>
          <option value="fairycore">🌿 Fairy Lost in the Internet</option>
        </select>
      </div>

      {/* Anything Special Input */}
      <div>
        <label htmlFor="special" className="block text-sm font-medium text-gray-300 mb-2">
          Aapke baare mein kuch special?
        </label>
        <textarea
          id="special" value={special} onChange={(e) => setSpecial(e.target.value)}
          placeholder="e.g., Meri ek billi hai jiska naam Nimbus hai"
          rows="3"
          className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-pink-500 outline-none transition"
        ></textarea>
      </div>

      {/* Submit Button */}
      <div>
        <button
          type="submit" disabled={isLoading}
          className="w-full flex justify-center items-center px-6 py-4 font-bold text-white bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg hover:from-purple-600 hover:to-pink-600 transition-all duration-300 ease-in-out disabled:opacity-50"
        >
          {isLoading ? 'Soch Raha Hu...' : 'Generate Names'}
        </button>
      </div>
    </form>
  );
}

export default NameForm;
