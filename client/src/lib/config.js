import { PUBLIC_SERVER_PORT, PUBLIC_SERVER_URL } from "$env/static/public";

export const serverUrl =
  process.env.NODE_ENV === "development"
    ? `http://localhost:${PUBLIC_SERVER_PORT}`
    : PUBLIC_SERVER_URL;
