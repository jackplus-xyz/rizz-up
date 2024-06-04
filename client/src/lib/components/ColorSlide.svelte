<script lang="ts">
	import { OnMount } from 'fractils';
	import ColorCubeButton from './ColorCubeButton.svelte';

	export let colors: string[];
</script>

<div class="grid w-full grid-cols-4 gap-2 md:grid-cols-6">
	{#each colors as color, index}
		<OnMount>
			<ColorCubeButton {color} duration={250 * index} on:colorSelected />
		</OnMount>
	{/each}
</div>
