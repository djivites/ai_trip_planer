import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { MapPin, Calendar, Wallet, Compass, Plane } from 'lucide-react';
import type { TripRequest } from '../api/trips';
import clsx from 'clsx';

interface TravelFormProps {
    onSubmit: (data: TripRequest) => void;
    isLoading: boolean;
}

export const TravelForm: React.FC<TravelFormProps> = ({ onSubmit, isLoading }) => {
    const [step, setStep] = useState(0);
    const [formData, setFormData] = useState<TripRequest>({
        destination: '',
        start_location: '',
        days: 5,
        budget: 'Medium',
        style: 'Balanced',
    });

    const handleChange = (field: keyof TripRequest, value: any) => {
        setFormData(prev => ({ ...prev, [field]: value }));
    };

    const nextStep = () => setStep(s => s + 1);
    const prevStep = () => setStep(s => s - 1);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSubmit(formData);
    };

    const steps = [
        {
            title: "Where to?",
            icon: MapPin,
            content: (
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm text-slate-400 mb-1">Destination</label>
                        <input
                            type="text"
                            placeholder="e.g. Paris, Japan"
                            className="w-full bg-slate-800 border border-slate-700 rounded-lg p-3 focus:ring-2 focus:ring-sky-500 outline-none transition-all"
                            value={formData.destination}
                            onChange={e => handleChange('destination', e.target.value)}
                            autoFocus
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-slate-400 mb-1">Starting From</label>
                        <input
                            type="text"
                            placeholder="e.g. New York"
                            className="w-full bg-slate-800 border border-slate-700 rounded-lg p-3 focus:ring-2 focus:ring-sky-500 outline-none transition-all"
                            value={formData.start_location}
                            onChange={e => handleChange('start_location', e.target.value)}
                        />
                    </div>
                </div>
            )
        },
        {
            title: "How long?",
            icon: Calendar,
            content: (
                <div>
                    <label className="block text-sm text-slate-400 mb-4">Duration (Days): {formData.days}</label>
                    <input
                        type="range"
                        min="1" max="30"
                        className="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-sky-500"
                        value={formData.days}
                        onChange={e => handleChange('days', parseInt(e.target.value))}
                    />
                    <div className="flex justify-between text-xs text-slate-500 mt-2">
                        <span>1 Day</span>
                        <span>30 Days</span>
                    </div>
                </div>
            )
        },
        {
            title: "Your Style",
            icon: Compass,
            content: (
                <div className="grid grid-cols-3 gap-3">
                    {['Relaxed', 'Balanced', 'Adventure'].map((s) => (
                        <button
                            key={s}
                            type="button"
                            onClick={() => handleChange('style', s)}
                            className={clsx(
                                "p-4 rounded-xl border transition-all text-sm font-medium",
                                formData.style === s
                                    ? "bg-sky-500/20 border-sky-500 text-sky-400"
                                    : "bg-slate-800 border-slate-700 hover:bg-slate-750 text-slate-300"
                            )}
                        >
                            {s}
                        </button>
                    ))}
                </div>
            )
        },
        {
            title: "Budget",
            icon: Wallet,
            content: (
                <div className="grid grid-cols-3 gap-3">
                    {['Low', 'Medium', 'High'].map((b) => (
                        <button
                            key={b}
                            type="button"
                            onClick={() => handleChange('budget', b)}
                            className={clsx(
                                "p-4 rounded-xl border transition-all text-sm font-medium",
                                formData.budget === b
                                    ? "bg-emerald-500/20 border-emerald-500 text-emerald-400"
                                    : "bg-slate-800 border-slate-700 hover:bg-slate-750 text-slate-300"
                            )}
                        >
                            {b}
                        </button>
                    ))}
                </div>
            )
        }
    ];

    return (
        <div className="glass-panel w-full max-w-md mx-auto relative overflow-hidden min-h-[400px] flex flex-col">
            <div className="absolute top-0 left-0 w-full h-1 bg-slate-800">
                <motion.div
                    className="h-full bg-sky-500"
                    initial={{ width: 0 }}
                    animate={{ width: `${((step + 1) / steps.length) * 100}%` }}
                />
            </div>

            <div className="flex-1 flex flex-col justify-center p-2">
                <AnimatePresence mode="wait">
                    <motion.div
                        key={step}
                        initial={{ x: 20, opacity: 0 }}
                        animate={{ x: 0, opacity: 1 }}
                        exit={{ x: -20, opacity: 0 }}
                        transition={{ duration: 0.2 }}
                        className="space-y-6"
                    >
                        <div className="flex items-center gap-3 mb-6">
                            <div className="p-3 bg-sky-500/10 rounded-full text-sky-400">
                                {React.createElement(steps[step].icon, { size: 24 })}
                            </div>
                            <h2 className="text-2xl font-bold">{steps[step].title}</h2>
                        </div>

                        {steps[step].content}

                    </motion.div>
                </AnimatePresence>
            </div>

            <div className="flex justify-between mt-8 pt-4 border-t border-white/5">
                <button
                    type="button"
                    onClick={prevStep}
                    disabled={step === 0}
                    className={clsx("text-sm text-slate-400 hover:text-white transition-colors", step === 0 && "opacity-0")}
                >
                    Back
                </button>

                {step < steps.length - 1 ? (
                    <button
                        type="button"
                        onClick={nextStep}
                        className="bg-white text-slate-900 px-6 py-2 rounded-full font-semibold hover:bg-slate-200 transition-colors"
                    >
                        Next
                    </button>
                ) : (
                    <button
                        onClick={handleSubmit}
                        disabled={isLoading}
                        className="bg-sky-500 text-white px-6 py-2 rounded-full font-semibold hover:bg-sky-600 transition-colors flex items-center gap-2"
                    >
                        {isLoading ? 'Planning...' : 'Start Journey'}
                        {!isLoading && <Plane size={16} />}
                    </button>
                )}
            </div>
        </div>
    );
};
