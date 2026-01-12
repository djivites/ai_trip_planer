import React from 'react';
import ReactMarkdown from 'react-markdown';
import { motion } from 'framer-motion';
import { ArrowLeft, Bot, CheckCircle } from 'lucide-react';

interface TripResultProps {
    result: Array<{ agent: string; content: string }>;
    onReset: () => void;
}

export const TripResult: React.FC<TripResultProps> = ({ result, onReset }) => {
    return (
        <div className="max-w-5xl mx-auto p-6 pb-20">
            <motion.button
                onClick={onReset}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="mb-8 flex items-center gap-2 text-slate-400 hover:text-white transition-colors group"
            >
                <div className="p-2 bg-slate-800 rounded-full group-hover:bg-slate-700 transition-colors">
                    <ArrowLeft size={20} />
                </div>
                <span>Plan Another Trip</span>
            </motion.button>

            <div className="space-y-8">
                {result.map((item, index) => (
                    <motion.div
                        key={index}
                        initial={{ opacity: 0, y: 30 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.15, duration: 0.5 }}
                        className="glass-panel border-l-4 border-l-sky-500 overflow-hidden"
                    >
                        <div className="flex items-center gap-3 mb-4 pb-4 border-b border-white/5">
                            <div className="bg-sky-500/10 p-2 rounded-lg text-sky-400">
                                <Bot size={24} />
                            </div>
                            <h3 className="text-xl font-bold text-sky-100">{item.agent}</h3>
                        </div>

                        <div className="prose prose-invert prose-headings:text-sky-300 prose-a:text-sky-400 prose-strong:text-white max-w-none text-slate-300 leading-relaxed">
                            <ReactMarkdown>{item.content}</ReactMarkdown>
                        </div>
                    </motion.div>
                ))}
            </div>

            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: result.length * 0.2 }}
                className="mt-12 text-center"
            >
                <div className="inline-flex items-center gap-2 px-6 py-3 bg-emerald-500/10 text-emerald-400 rounded-full border border-emerald-500/20">
                    <CheckCircle size={20} />
                    <span className="font-semibold">Itinerary Complete</span>
                </div>
            </motion.div>
        </div>
    );
};
