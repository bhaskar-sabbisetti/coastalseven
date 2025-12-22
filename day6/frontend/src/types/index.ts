export interface User {
    id: string;
    email: string;
    full_name: string;
    role: string;
    is_active: boolean;
    created_at: string;
}

export interface AuthResponse {
    access_token: string;
    refresh_token: string;
    token_type: string;
}

export interface LoginRequest {
    username: string; // OAuth2PasswordRequestForm expects username
    password: string;
}

export interface SignupRequest {
    email: string;
    password: string;
    full_name: string;
}
