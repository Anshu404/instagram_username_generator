
//this was my older file


// /** @type {import('tailwindcss').Config} */
// export default {
//   content: [],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }

//you want me to update this with this one 

    /** @type {import('tailwindcss').Config} */
    export default {
      content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}", // Is line ko add/update karein
      ],
      theme: {
        extend: {},
      },
      plugins: [],
    }
    