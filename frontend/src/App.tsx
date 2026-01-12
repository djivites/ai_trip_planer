import { useState } from 'react';
import { TravelForm } from './components/TravelForm';
import { TripResult } from './components/TripResult';
import { planTrip, type TripRequest, type TripResponse } from './api/trips';
import { motion, AnimatePresence } from 'framer-motion';
import { Plane } from 'lucide-react';

function App() {
  const [result, setResult] = useState<TripResponse['result'] | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handlePlanTrip = async (data: TripRequest) => {
    setIsLoading(true);
    try {
      const response = await planTrip(data);
      setResult(response.result);
    } catch (error) {
      console.error(error);
      alert("Failed to plan trip. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-slate-900 via-slate-950 to-black text-white relative">
      {/* Background decoration */}
      <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1488085061387-422e29b40080?q=80&w=2000&auto=format&fit=crop')] opacity-5 bg-cover bg-center pointer-events-none" />

      <main className="relative z-10 container mx-auto px-4 py-8 min-h-screen flex flex-col">
        <header className="mb-12 text-center pt-10">
          <div className="inline-flex items-center justify-center p-3 bg-white/5 rounded-full mb-6 ring-1 ring-white/10 backdrop-blur-sm">
            <Plane className="text-sky-400 mr-2" />
            <span className="font-semibold tracking-wide uppercase text-sm">AI Itinerary Agent</span>
          </div>
          <h1 className="text-5xl md:text-7xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-white to-slate-500 mb-6 pb-2">
            Plan your next <br />
            <span className="text-sky-400">Great Journey</span>
          </h1>
          <p className="text-slate-400 max-w-lg mx-auto text-lg">
            Tell us your preferences and let our AI agents orchestrate the perfect travel experience for you.
          </p>
        </header>

        <div className="flex-1 flex flex-col justify-center pb-20">
          <AnimatePresence mode="wait">
            {isLoading ? (
              <motion.div
                key="loading"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="flex flex-col items-center justify-center space-y-8"
              >
                <div className="relative w-32 h-32">
                  <div className="absolute inset-0 border-4 border-slate-800 rounded-full" />
                  <div className="absolute inset-0 border-4 border-t-sky-500 rounded-full animate-spin" />
                  <Plane className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-sky-500 animate-pulse" size={40} />
                </div>
                <div className="text-center space-y-2">
                  <h3 className="text-xl font-medium text-white">Crafting your itinerary...</h3>
                  <p className="text-slate-500">Our agents are researching flights, hotels, and attractions.</p>
                </div>
              </motion.div>
            ) : result ? (
              <TripResult key="result" result={result} onReset={() => setResult(null)} />
            ) : (
              <motion.div
                key="form"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
              >
                <TravelForm onSubmit={handlePlanTrip} isLoading={isLoading} />
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        <footer className="text-center text-slate-600 text-sm py-8">
          Built with CrewAI & FastAPI
        </footer>
      </main>
    </div>
  );
}

export default App;
