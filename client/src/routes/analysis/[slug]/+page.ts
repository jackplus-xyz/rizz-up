import { serverUrl } from "$lib/config.js";
import { error } from "@sveltejs/kit";
import type { PageLoad } from "./$types";

export type PageData = {
  analysis: {
    skinTone: string;
    colors: string[];
    season: string;
  };
};

export const load: PageLoad = async ({ params, fetch }) => {
  const hexPattern = /^[0-9a-fA-F]{6}$/;
  const skinTone = decodeURIComponent(params.slug);

  if (
    skinTone.length != 6 ||
    skinTone.includes("\0") ||
    !hexPattern.test(skinTone)
  ) {
    throw error(400, "Invalid request");
  }

  try {
    const response = await fetch(`${serverUrl}/palette/hex/${skinTone}`);
    if (!response.ok) {
      throw error(response.status, "Failed to fetch palette");
    }

    const data: PageData = { analysis: await response.json() };
    return data;
  } catch (err) {
    console.error(err);
    throw error(500, "Failed to fetch palette");
  }
};
