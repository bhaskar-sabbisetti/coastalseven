import React from 'react';
import { Link } from 'react-router-dom';
import { Menu, X, Terminal } from 'lucide-react';

export const Navbar = () => {
    const [isOpen, setIsOpen] = React.useState(false);

    const scrollToSection = (id: string) => {
        setIsOpen(false);
        const element = document.getElementById(id);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    };

    return (
        <nav className="bg-white/80 backdrop-blur-md border-b border-gray-100 shadow-sm fixed w-full top-0 z-50 transition-all duration-300">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16">
                    <div className="flex items-center">
                        <Link to="/" className="flex-shrink-0 flex items-center gap-2" onClick={() => window.scrollTo(0, 0)}>
                            <div className="bg-blue-600 p-1.5 rounded-lg">
                                <Terminal size={20} className="text-white" />
                            </div>
                            <span className="text-xl font-bold text-gray-900 tracking-tight">
                                Bhaskar<span className="text-blue-600">.dev</span>
                            </span>
                        </Link>
                    </div>

                    <div className="hidden md:flex md:items-center md:space-x-6">
                        {['About', 'Education', 'Skills', 'Projects', 'Certifications'].map((item) => (
                            <button
                                key={item}
                                onClick={() => scrollToSection(item.toLowerCase())}
                                className="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium transition-colors"
                            >
                                {item}
                            </button>
                        ))}
                        <button
                            onClick={() => scrollToSection('contact')}
                            className="text-gray-600 hover:text-blue-600 px-3 py-2 text-sm font-medium transition-colors"
                        >
                            Contact
                        </button>

                        <div className="h-6 w-px bg-gray-200 mx-2"></div>
                    </div>

                    {/* Mobile menu button */}
                    <div className="flex items-center md:hidden">
                        <button
                            onClick={() => setIsOpen(!isOpen)}
                            className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none"
                        >
                            {isOpen ? <X size={24} /> : <Menu size={24} />}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile Menu */}
            {isOpen && (
                <div className="md:hidden bg-white border-t border-gray-100 animate-in slide-in-from-top-4">
                    <div className="pt-2 pb-3 space-y-1">
                        {['About', 'Education', 'Skills', 'Projects', 'Certifications', 'Contact'].map((item) => (
                            <button
                                key={item}
                                onClick={() => scrollToSection(item.toLowerCase())}
                                className="block w-full text-left px-4 py-3 text-base font-medium text-gray-500 hover:text-gray-900 hover:bg-gray-50 border-l-4 border-transparent hover:border-blue-600"
                            >
                                {item}
                            </button>
                        ))}
                    </div>
                </div>
            )}
        </nav>
    );
};
