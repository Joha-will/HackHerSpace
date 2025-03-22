/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'templates/*.html',
    './home/templates/home/*.html',
'./templates/**/*.html',
    './**/templates/**/*.html',
    './static/js/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

