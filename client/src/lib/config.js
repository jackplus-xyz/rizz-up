const ENV = import.meta.env.VITE_ENV;
const PORT = import.meta.env.VITE_SERVER_PORT;
const PROD_SERVER_URL = import.meta.env.VITE_PROD_SERVER_URL;
const isDevelopment = ENV === 'development';
export const serverUrl = isDevelopment ? `http://localhost:${PORT}` : PROD_SERVER_URL;
