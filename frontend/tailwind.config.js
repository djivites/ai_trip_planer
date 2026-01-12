/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                journey: {
                    dark: '#0f172a',
                    light: '#f8fafc',
                    accent: '#38bdf8', // Light blue
                }
            },
            animation: {
                'fly': 'fly 3s linear infinite',
            },
            keyframes: {
                fly: {
                    '0%': { transform: 'translateX(-100%)' },
                    '100%': { transform: 'translateX(100%)' },
                }
            }
        },
    },
    plugins: [],
}
