import axios from 'axios';
import { getToken } from '@/services/auth'

const instance = axios.create({
    baseURL: 'http://localhost:8000/api/', // Базовый URL вашего API
    headers: {
        'Content-Type': 'application/json'
    }
});

instance.interceptors.request.use(
    config => {
        const token = getToken();
        if (token) {
            config.headers.Authorization = token;
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
)

export default instance;