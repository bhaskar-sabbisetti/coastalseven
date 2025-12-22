import api from './api';
import type { LoginRequest, SignupRequest, AuthResponse, User } from '../types';

export const authService = {
    login: async (data: LoginRequest) => {
        // FastAPI OAuth2PasswordRequestForm expects form-data
        const formData = new FormData();
        formData.append('username', data.username);
        formData.append('password', data.password);

        const response = await api.post<AuthResponse>('/auth/login', formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
        });
        return response.data;
    },

    signup: async (data: SignupRequest) => {
        const response = await api.post<User>('/auth/signup', data);
        return response.data;
    },

    getCurrentUser: async () => {
        const response = await api.get<User>('/users/me');
        return response.data;
    },

    googleLogin: async (credential: string) => {
        const response = await api.post<AuthResponse>('/auth/google', { credential });
        return response.data;
    },
};
