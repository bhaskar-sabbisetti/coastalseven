import React from 'react';
import { Navbar } from './Navbar';
import { Outlet } from 'react-router-dom';

export const Layout = () => {
    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <main className="pt-16">
                <Outlet />
            </main>
        </div>
    );
};
