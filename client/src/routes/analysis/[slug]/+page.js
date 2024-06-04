import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
export function load({ params }) {
	const hexPattern = /^[0-9a-fA-F]{6}$/;
	const decodedSlug = decodeURIComponent(params.slug);

	if (decodedSlug.length != 6) {
		throw error(400, 'Invalid request');
	}

	// Check for null bytes
	if (decodedSlug.includes('\0')) {
		throw error(400, 'Invalid request');
	}

	const isValidHex = hexPattern.test(decodedSlug);
	if (isValidHex) {
		return {
			slug: decodedSlug
		};
	}

	throw error(404, 'Not found');
}
