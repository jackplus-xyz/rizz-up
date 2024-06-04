<script lang="ts">
	import { cubicOut } from 'svelte/easing';
	import { fly, fade } from 'svelte/transition';

	export let color: string;
	export let duration = 0;
	export let translateY = 0;
	export let translateX = 0;
	export let label = color.toUpperCase();

	$: textColor = getLuminance(color) > 0.5 ? 'black' : 'white';

	function getLuminance(hexColor: string): number {
		const rgb = hexToRgb(hexColor);
		if (!rgb) return 0;

		const [r, g, b] = rgb.map((c) => {
			c /= 255;
			return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
		});

		return 0.2126 * r + 0.7152 * g + 0.0722 * b;
	}

	function hexToRgb(hex: string): number[] | null {
		const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
		return result
			? [parseInt(result[1], 16), parseInt(result[2], 16), parseInt(result[3], 16)]
			: null;
	}
</script>

<div
	class="group relative aspect-square w-full rounded-xl transition-all duration-500 ease-in-out
	hover:scale-105 md:rounded-3xl"
	style="background-color: {color};"
	in:fly={{
		x: translateX,
		y: translateY,
		duration: duration,
		easing: cubicOut
	}}
>
	<span
		class="duration-250 absolute inset-0 hidden items-center justify-center text-base opacity-0 transition-opacity ease-in-out group-hover:opacity-100 md:flex"
		style="color: {textColor};"
		in:fade
	>
		{label}
	</span>
</div>
