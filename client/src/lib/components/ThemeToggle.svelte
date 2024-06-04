<script>
	import { theme } from '$lib/stores';
	import { BROWSER } from 'esm-env';
	import { onDestroy } from 'svelte';
	import LineMdSunnyOutlineLoop from '~icons/line-md/sunny-outline-loop';
	import LineMdMoonAltLoop from '~icons/line-md/moon-alt-loop';

	export let label = 'Dark mode';
	export let outline = true;

	function toggle() {
		const upcoming_theme = $theme.current === 'light' ? 'dark' : 'light';

		if (
			upcoming_theme ===
			(window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
		) {
			// Switch the preference to `system`
			$theme.preference = 'system';
		} else {
			// Switch the preference to `light` or `dark`
			$theme.preference = upcoming_theme;
		}

		$theme.current = upcoming_theme;
	}

	/** @param {MediaQueryListEvent} e */
	const cb = (e) =>
		theme.set({ preference: $theme.preference, current: e.matches ? 'dark' : 'light' });

	/** @type {MediaQueryList} */
	let query;

	$: {
		if (!BROWSER) break $;

		query?.removeEventListener('change', cb);

		if ($theme.preference === 'system') {
			query = window.matchMedia('(prefers-color-scheme: dark)');
			query.addEventListener('change', cb);
		}
	}

	onDestroy(() => query?.removeEventListener('change', cb));
</script>

<button
	class="button text-primary-background flex space-x-4 rounded-full border-muted-foreground p-2"
	class:border={outline}
	class:border-0={!outline}
	on:click={toggle}
	type="button"
	aria-pressed={$theme.current === 'dark' ? 'true' : 'false'}
	aria-label={label}
>
	<span class:checked={$theme.current === 'dark'}>
		{#if BROWSER}
			{#if $theme.current === 'dark'}
				<LineMdSunnyOutlineLoop />
			{:else}
				<LineMdMoonAltLoop />
			{/if}
		{/if}
	</span>
</button>
