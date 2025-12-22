import React, { useEffect } from 'react';
import { useAuthStore } from '../store/authStore';
import { useNavigate } from 'react-router-dom';

export const Dashboard = () => {
    const { user, checkAuth, isLoading } = useAuthStore();
    const navigate = useNavigate();

    useEffect(() => {
        checkAuth();
    }, [checkAuth]);

    if (isLoading) return <div className="p-8 text-center">Loading...</div>;

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
            <p className="mt-1 text-gray-500">Welcome back, {user?.full_name}!</p>

            <div className="mt-8 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
                {/* Stats Card */}
                <div className="bg-white overflow-hidden shadow rounded-lg border border-gray-100">
                    <div className="p-5">
                        <div className="flex items-center">
                            <div className="flex-shrink-0 bg-blue-100 rounded-md p-3">
                                <svg className="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                                </svg>
                            </div>
                            <div className="ml-5 w-0 flex-1">
                                <dl>
                                    <dt className="text-sm font-medium text-gray-500 truncate">Enrolled Courses</dt>
                                    <dd className="text-lg font-medium text-gray-900">0</dd>
                                </dl>
                            </div>
                        </div>
                    </div>
                    <div className="bg-gray-50 px-5 py-3">
                        <div className="text-sm">
                            <a href="#" className="font-medium text-blue-700 hover:text-blue-900">
                                View all
                            </a>
                        </div>
                    </div>
                </div>

                {/* More cards... */}
                <div className="bg-white overflow-hidden shadow rounded-lg border border-gray-100 p-6 flex items-center justify-center text-gray-400">
                    <p>More modules coming soon...</p>
                </div>
            </div>
        </div>
    );
};
