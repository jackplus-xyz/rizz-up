<script>
	import GuidanceLeft2ShortArrow from '~icons/guidance/left-2-short-arrow';

	export let link = '/';
	export let text = 'Home';
</script>

<a href={link} class="group relative flex items-center">
	{text}
	<span class="ml-2 transition-all group-hover:translate-x-2 md:ml-4">
		<GuidanceLeft2ShortArrow />
	</span>
</a>
