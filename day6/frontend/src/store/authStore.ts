import { create } from 'zustand';
import type { User } from '../types';
import { authService } from '../services/auth';

interface AuthState {
    user: User | null;
    token: string | null;
    isAuthenticated: boolean;
    isLoading: boolean;
    login: (token: string) => void;
    logout: () => void;
    setUser: (user: User) => void;
    checkAuth: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set, get) => ({
    user: null,
    token: localStorage.getItem('token'),
    isAuthenticated: !!localStorage.getItem('token'),
    isLoading: false,

    login: (token: string) => {
        localStorage.setItem('token', token);
        set({ token, isAuthenticated: true });
    },

    logout: () => {
        localStorage.removeItem('token');
        set({ user: null, token: null, isAuthenticated: false });
    },

    setUser: (user: User) => set({ user }),

    checkAuth: async () => {
        const { token } = get();
        if (!token) return;

        set({ isLoading: true });
        try {
            const user = await authService.getCurrentUser();
            set({ user, isAuthenticated: true });
        } catch (error) {
            console.error("Auth check failed", error);
            get().logout();
        } finally {
            set({ isLoading: false });
        }
    },
}));
