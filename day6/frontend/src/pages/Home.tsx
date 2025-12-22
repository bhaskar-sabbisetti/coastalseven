import React from 'react';
import { motion } from 'framer-motion';
import {
    ArrowRight, Database, Shield, Code,
    Github, Linkedin, Mail, Terminal, Layers, Cpu,
    Award, User, Phone, Globe
} from 'lucide-react';
import { Link } from 'react-router-dom';

export const Home = () => {
    return (
        <div className="bg-white">
            {/* Hero Section */}
            <section id="about" className="relative min-h-screen flex items-center justify-center bg-gray-900 text-white overflow-hidden py-20">
                <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-blue-900/20 via-gray-900 to-gray-900"></div>

                <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center z-10">
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ duration: 0.8 }}
                        className="mb-8 inline-block"
                    >
                        <div className="bg-gray-800/50 backdrop-blur-sm px-4 py-2 rounded-full border border-gray-700 text-blue-400 text-sm font-medium">
                            Python Developer | AI/ML Enthusiast
                        </div>
                    </motion.div>

                    <motion.h1
                        initial={{ opacity: 0, y: 30 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.2, duration: 0.8 }}
                        className="text-5xl md:text-7xl font-bold tracking-tight mb-6 bg-gradient-to-r from-white via-gray-200 to-gray-400 text-transparent bg-clip-text"
                    >
                        Sabbisetti Bhaskar
                    </motion.h1>

                    <motion.p
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.4, duration: 0.8 }}
                        className="text-lg md:text-xl text-gray-400 max-w-4xl mx-auto mb-10 leading-relaxed font-light"
                    >
                        Detail-oriented and passionate Python Developer with strong foundations in software development, data analysis, and machine learning.
                        Proficient in <span className="text-white font-medium">Python, SQL, and Data Structures</span>, with hands-on experience in building ML models, NLP-based applications, and computer vision projects.
                    </motion.p>

                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.6 }}
                        className="flex flex-wrap justify-center gap-4"
                    >
                        <a href="mailto:bhaskarsabbisetti@gmail.com" className="bg-blue-600 hover:bg-blue-500 text-white px-8 py-3 rounded-full font-semibold transition-all hover:scale-105 flex items-center gap-2">
                            <Mail size={20} /> bhaskarsabbisetti@gmail.com
                        </a>
                        <a href="tel:+916281007255" className="bg-gray-800 hover:bg-gray-700 text-white px-8 py-3 rounded-full font-semibold transition-all border border-gray-700 flex items-center gap-2">
                            <Phone size={20} /> +91 6281007255
                        </a>
                    </motion.div>
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.8 }}
                        className="mt-8 flex justify-center gap-6 text-gray-400"
                    >
                        <a href="https://linkedin.com/in/sabbisetti-bhaskar-82400a2a4/" target="_blank" rel="noreferrer" className="hover:text-blue-400 transition transform hover:scale-110"><Linkedin size={28} /></a>
                        <a href="https://github.com/bhaskarsabbisetti" target="_blank" rel="noreferrer" className="hover:text-white transition transform hover:scale-110"><Github size={28} /></a>
                    </motion.div>
                </div>
            </section>

            {/* Education Section */}
            <section id="education" className="py-20 bg-gray-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center mb-16">
                        <h2 className="text-blue-600 font-semibold tracking-wide uppercase">Academic Background</h2>
                        <h3 className="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
                            Education
                        </h3>
                    </div>

                    <div className="max-w-4xl mx-auto space-y-8">
                        <motion.div
                            whileHover={{ scale: 1.02 }}
                            className="bg-white p-8 rounded-2xl shadow-lg border-l-4 border-blue-600 flex flex-col md:flex-row justify-between items-start md:items-center"
                        >
                            <div>
                                <h4 className="text-xl font-bold text-gray-900">Mallareddy Institute of Technology and Science, Telangana</h4>
                                <p className="text-gray-600 mt-1">Bachelor of Technology (B.Tech), <span className="text-blue-600 font-semibold">Computer Science Engineering (AI & ML)</span></p>
                            </div>
                            <div className="mt-4 md:mt-0 text-right">
                                <span className="block text-lg font-bold text-gray-900">2021 - 2025</span>
                                <span className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full mt-1">CGPA: 7.5/10</span>
                            </div>
                        </motion.div>

                        <motion.div
                            whileHover={{ scale: 1.02 }}
                            className="bg-white p-8 rounded-2xl shadow-lg border-l-4 border-indigo-600 flex flex-col md:flex-row justify-between items-start md:items-center"
                        >
                            <div>
                                <h4 className="text-xl font-bold text-gray-900">V.S.N Junior College</h4>
                                <p className="text-gray-600 mt-1">Intermediate (MPC)</p>
                            </div>
                            <div className="mt-4 md:mt-0 text-right">
                                <span className="block text-lg font-bold text-gray-900">2019 - 2021</span>
                                <span className="inline-block bg-indigo-100 text-indigo-800 text-xs px-2 py-1 rounded-full mt-1">Marks: 887/1000</span>
                            </div>
                        </motion.div>
                    </div>
                </div>
            </section>

            {/* Skills Section */}
            <section id="skills" className="py-20 bg-white">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center mb-16">
                        <h2 className="text-blue-600 font-semibold tracking-wide uppercase">Technical Arsenal</h2>
                        <h3 className="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
                            Skills & Expertise
                        </h3>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                        {/* Programming Languages */}
                        <div className="bg-gray-50 p-6 rounded-2xl border border-gray-100">
                            <h4 className="flex items-center gap-2 font-bold text-gray-900 mb-4"><Code className="text-blue-500" /> Programming Languages</h4>
                            <div className="flex flex-wrap gap-2">
                                {['Python', 'C', 'JavaScript', 'HTML/CSS', 'SQL'].map(s => (
                                    <span key={s} className="bg-white px-3 py-1 rounded-full text-sm text-gray-700 shadow-sm border border-gray-200">{s}</span>
                                ))}
                            </div>
                        </div>

                        {/* AI/ML */}
                        <div className="bg-gray-50 p-6 rounded-2xl border border-gray-100">
                            <h4 className="flex items-center gap-2 font-bold text-gray-900 mb-4"><Cpu className="text-purple-500" /> Machine Learning & NLP</h4>
                            <div className="flex flex-wrap gap-2">
                                {['Scikit-learn', 'NLTK', 'OpenCV', 'Pandas', 'NumPy', 'Computer Vision'].map(s => (
                                    <span key={s} className="bg-white px-3 py-1 rounded-full text-sm text-gray-700 shadow-sm border border-gray-200">{s}</span>
                                ))}
                            </div>
                        </div>

                        {/* Frameworks & Databases */}
                        <div className="bg-gray-50 p-6 rounded-2xl border border-gray-100">
                            <h4 className="flex items-center gap-2 font-bold text-gray-900 mb-4"><Database className="text-green-500" /> Frameworks & DBs</h4>
                            <div className="flex flex-wrap gap-2">
                                {['Django', 'FastAPI', 'React', 'MySQL', 'PostgreSQL', 'MongoDB'].map(s => (
                                    <span key={s} className="bg-white px-3 py-1 rounded-full text-sm text-gray-700 shadow-sm border border-gray-200">{s}</span>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* Projects Section */}
            <section id="projects" className="py-20 bg-gray-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center mb-16">
                        <h2 className="text-blue-600 font-semibold tracking-wide uppercase">Practical Experience</h2>
                        <h3 className="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
                            Featured Projects
                        </h3>
                    </div>

                    <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
                        {/* Sepnoty */}
                        <motion.div whileHover={{ y: -5 }} className="bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-100 flex flex-col">
                            <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-6 text-white">
                                <Terminal size={32} className="mb-4" />
                                <h4 className="text-xl font-bold">Sepnoty Learning Platform</h4>
                                <p className="text-blue-100 text-sm mt-1">Enterprise Backend Architecture</p>
                            </div>
                            <div className="p-6 flex-1 flex flex-col">
                                <p className="text-gray-600 text-sm mb-4 flex-1">
                                    Microservices-ready system with <strong>FastAPI, AsyncPG, MongoDB, Redis, and OAuth2</strong>. Features hybrid database design and RBAC security.
                                </p>
                                <Link to="/login" className="text-blue-600 font-semibold hover:text-blue-800 flex items-center gap-1 mt-auto">
                                    View Live <ArrowRight size={16} />
                                </Link>
                            </div>
                        </motion.div>

                        {/* Drug Recommendation */}
                        <motion.div whileHover={{ y: -5 }} className="bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-100 flex flex-col">
                            <div className="bg-gradient-to-r from-green-600 to-emerald-600 p-6 text-white">
                                <Shield size={32} className="mb-4" />
                                <h4 className="text-xl font-bold">Drug Recommendation System</h4>
                                <p className="text-green-100 text-sm mt-1">ML-based Healthcare Tool</p>
                            </div>
                            <div className="p-6 flex-1 flex flex-col">
                                <p className="text-gray-600 text-sm mb-4 flex-1">
                                    Developed using <strong>Python, Scikit-learn, NLTK, Tkinter</strong>. Applied TF-IDF for text feature extraction and ML models for drug suggestions based on symptoms.
                                </p>
                                <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded w-fit">Machine Learning</span>
                            </div>
                        </motion.div>

                        {/* Cartoon Image Converter */}
                        <motion.div whileHover={{ y: -5 }} className="bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-100 flex flex-col">
                            <div className="bg-gradient-to-r from-purple-600 to-pink-600 p-6 text-white">
                                <Layers size={32} className="mb-4" />
                                <h4 className="text-xl font-bold">Cartoon Image Converter</h4>
                                <p className="text-purple-100 text-sm mt-1">Computer Vision Tool</p>
                            </div>
                            <div className="p-6 flex-1 flex flex-col">
                                <p className="text-gray-600 text-sm mb-4 flex-1">
                                    Built with <strong>Python, OpenCV, NumPy</strong>. Implemented bilateral filtering and adaptive thresholding to transform real-life images into cartoon-style visuals.
                                </p>
                                <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded w-fit">Computer Vision</span>
                            </div>
                        </motion.div>
                    </div>
                </div>
            </section>

            {/* Certifications & Soft Skills */}
            <section id="certifications" className="py-20 bg-white">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="grid md:grid-cols-2 gap-16">
                        <div>
                            <h3 className="text-2xl font-bold text-gray-900 mb-8 flex items-center gap-2">
                                <Award className="text-yellow-500" /> Certifications
                            </h3>
                            <ul className="space-y-4">
                                {[
                                    'Python Programming – CTI (Center for Training & Institute)',
                                    'Machine Learning – Internshala Trainings',
                                    'JavaScript Programming – GUVI',
                                    'HTML & CSS – GUVI'
                                ].map((cert, i) => (
                                    <motion.li
                                        key={i}
                                        initial={{ opacity: 0, x: -20 }}
                                        whileInView={{ opacity: 1, x: 0 }}
                                        transition={{ delay: i * 0.1 }}
                                        className="flex items-start gap-3 p-4 bg-gray-50 rounded-lg border border-gray-100 hover:shadow-md transition-shadow"
                                    >
                                        <div className="h-2 w-2 rounded-full bg-blue-500 mt-2 flex-shrink-0"></div>
                                        <span className="text-gray-700 font-medium">{cert}</span>
                                    </motion.li>
                                ))}
                            </ul>
                        </div>

                        <div>
                            <h3 className="text-2xl font-bold text-gray-900 mb-8 flex items-center gap-2">
                                <User className="text-indigo-500" /> Soft Skills
                            </h3>
                            <div className="flex flex-wrap gap-3">
                                {['Communication', 'Leadership', 'Problem Solving', 'Adaptability', 'Time Management', 'Creativity'].map((skill, i) => (
                                    <motion.span
                                        key={i}
                                        whileHover={{ scale: 1.1 }}
                                        className="bg-indigo-50 text-indigo-700 px-4 py-2 rounded-full font-medium border border-indigo-100 cursor-default"
                                    >
                                        {skill}
                                    </motion.span>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* Contact Section */}
            <section id="contact" className="py-20 bg-gray-900 text-white">
                <div className="max-w-4xl mx-auto px-4">
                    <div className="text-center mb-12">
                        <h2 className="text-3xl font-bold mb-4">Ready to Scale?</h2>
                        <p className="text-xl text-gray-400">
                            I am available for Senior Backend Engineering roles. Let's build something world-class together.
                        </p>
                    </div>

                    <div className="grid md:grid-cols-2 gap-12">
                        {/* Contact Info */}
                        <div className="space-y-8">
                            <h3 className="text-2xl font-bold text-white">Get in Touch</h3>
                            <p className="text-gray-400">
                                Whether you have a question, a project proposal, or just want to say hi, I'll try my best to get back to you!
                            </p>

                            <div className="space-y-4">
                                <div className="flex items-center gap-4 text-gray-300">
                                    <Mail className="text-blue-500" /> bhaskarsabbisetti@gmail.com
                                </div>
                                <div className="flex items-center gap-4 text-gray-300">
                                    <Phone className="text-blue-500" /> +91 6281007255
                                </div>
                                <div className="flex items-center gap-4 text-gray-300">
                                    <Globe className="text-blue-500" /> Hyderabad, India
                                </div>
                            </div>

                            <div className="flex gap-6 pt-6">
                                <a href="https://github.com/bhaskarsabbisetti" target="_blank" rel="noreferrer" className="bg-gray-800 p-3 rounded-full hover:bg-blue-600 transition-colors"><Github size={20} /></a>
                                <a href="https://linkedin.com/in/sabbisetti-bhaskar-82400a2a4/" target="_blank" rel="noreferrer" className="bg-gray-800 p-3 rounded-full hover:bg-blue-600 transition-colors"><Linkedin size={20} /></a>
                            </div>
                        </div>

                        {/* Contact Form */}
                        <ContactForm />
                    </div>
                </div>
            </section>

            {/* Footer */}
            <footer className="bg-gray-900 text-white py-12 border-t border-gray-800">
                <div className="max-w-7xl mx-auto px-4 text-center">
                    <h2 className="text-2xl font-bold mb-4">Sabbisetti Bhaskar</h2>
                    <p className="text-gray-400 mb-8">Building the future with Python & AI</p>
                    <div className="flex justify-center gap-8 text-gray-400">
                        <a href="https://github.com/bhaskarsabbisetti" className="hover:text-white transition"><Github /></a>
                        <a href="https://linkedin.com/in/sabbisetti-bhaskar-82400a2a4/" className="hover:text-white transition"><Linkedin /></a>
                        <a href="mailto:bhaskarsabbisetti@gmail.com" className="hover:text-white transition"><Mail /></a>
                    </div>
                </div>
            </footer>
        </div>
    );
};

const ContactForm = () => {
    const [formData, setFormData] = React.useState({ name: '', email: '', message: '' });
    const [status, setStatus] = React.useState<'idle' | 'loading' | 'success' | 'error'>('idle');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setStatus('loading');
        try {
            const response = await fetch('http://localhost:8000/api/v1/contact/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            if (!response.ok) throw new Error('Failed to send');

            setStatus('success');
            setFormData({ name: '', email: '', message: '' });
        } catch (err) {
            setStatus('error');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="bg-gray-800 p-8 rounded-2xl border border-gray-700 space-y-6">
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Your Name</label>
                <input
                    type="text"
                    required
                    value={formData.name}
                    onChange={e => setFormData({ ...formData, name: e.target.value })}
                    className="w-full bg-gray-900 border border-gray-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-blue-500 transition-colors"
                    placeholder="John Doe"
                />
            </div>
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Email Address</label>
                <input
                    type="email"
                    required
                    value={formData.email}
                    onChange={e => setFormData({ ...formData, email: e.target.value })}
                    className="w-full bg-gray-900 border border-gray-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-blue-500 transition-colors"
                    placeholder="john@example.com"
                />
            </div>
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">Message</label>
                <textarea
                    rows={4}
                    required
                    value={formData.message}
                    onChange={e => setFormData({ ...formData, message: e.target.value })}
                    className="w-full bg-gray-900 border border-gray-600 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-blue-500 transition-colors"
                    placeholder="I'd like to discuss a project..."
                ></textarea>
            </div>

            <button
                type="submit"
                disabled={status === 'loading'}
                className="w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 rounded-lg transition-all flex justify-center items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
                {status === 'loading' ? (
                    'Sending...'
                ) : status === 'success' ? (
                    'Message Sent! ✅'
                ) : status === 'error' ? (
                    'Failed to Send ❌'
                ) : (
                    <>Send Message <ArrowRight size={18} /></>
                )}
            </button>
        </form>
    );
};
